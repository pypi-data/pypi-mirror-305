import socket
import threading
import uuid
import datetime
import logging
import mysql.connector
from cryptography.fernet import Fernet

from mysqlonsocket.configrations import FORMAT, HEARTBEAT_INTERVAL, ENCRYPTION_KEY
from mysqlonsocket.utils import setup_logger, secure_execute_query, encrypt_data, decrypt_data

cipher = Fernet(ENCRYPTION_KEY)

class Server:
    def __init__(self, server_host, server_port, db_host, db_user, db_pswd, db_name, log_dir=None):
        self.server_host = server_host
        self.server_port = server_port
        self.db_config = {
            'host': db_host,
            'user': db_user,
            'password': db_pswd,
            'database': db_name
        }
        self.log_dir = log_dir
        self.clients = {}

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.server_host, self.server_port))

        setup_logger(self.log_dir)
        logging.info(f"SERVER initialized at {datetime.datetime.now()}")
        print(f"SERVER initialized at {datetime.datetime.now()}")

    def handle(self, client, addr):
        client_id = str(uuid.uuid4())
        logging.info(f"Sending client ID {client_id} to client at {addr}")
        client.send(cipher.encrypt(client_id.encode(FORMAT)))

        self.clients[client_id] = {'address': addr, 'status': 'available', 'last_heartbeat': datetime.datetime.now()}

        try:
            with mysql.connector.connect(**self.db_config) as my_conn:
                with my_conn.cursor() as my_cursor:
                    while True:
                        client.settimeout(HEARTBEAT_INTERVAL)
                        logging.info(f"Waiting for query from client {client_id}")
                        encrypted_query = client.recv(4096)
                        if not encrypted_query:
                            logging.info(f"No query received from client {client_id}, closing connection.")
                            break
                        
                        query = decrypt_data(encrypted_query, cipher)

                        if query == b"HEARTBEAT":
                            logging.info(f"Received HEARTBEAT from client {client_id}")
                            self.clients[client_id]['last_heartbeat'] = datetime.datetime.now()
                            continue

                        data = secure_execute_query(my_cursor, query.decode(FORMAT))
                        encrypted_data = encrypt_data(data, cipher)
                        client.sendall(encrypted_data)
                        my_conn.commit()

        except mysql.connector.Error as err:
            client.send(cipher.encrypt(f"Database error: {err}".encode(FORMAT)))
        except socket.timeout:
            logging.warning(f"Client {client_id} timed out.")
        except (ConnectionResetError, BrokenPipeError):
            logging.warning(f"Connection issue with client {client_id}.")
        finally:
            self.clients[client_id]['status'] = 'disconnected'
            client.close()

    def start_server(self):
        logging.info(f"SERVER started listening at {datetime.datetime.now()}")
        self.server.listen()

        admin_thread = threading.Thread(target=self.handle_admin_commands)
        admin_thread.start()

        while True:
            client, addr = self.server.accept()
            logging.info(f"Connection from {addr} at {datetime.datetime.now()}")
            thread = threading.Thread(target=self.handle, args=(client, addr))
            thread.start()

    def stop_server(self):
        self.server.close()
        logging.info("Server stopped.")

    def handle_admin_commands(self):
        while True:
            command = input("Enter admin command: ")
            if command == "showclients":
                for client_id, info in self.clients.items():
                    logging.info(f"Client ID: {client_id}, Status: {info['status']}, Last Heartbeat: {info['last_heartbeat']}")
            elif command == "shutdown":
                self.stop_server()
                break

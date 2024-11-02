import socket
import threading
import time
import pickle
from cryptography.fernet import Fernet

from mysqlonsocket.configrations import FORMAT, HEARTBEAT_INTERVAL, ENCRYPTION_KEY
from mysqlonsocket.utils import encrypt_data, decrypt_data

cipher = Fernet(ENCRYPTION_KEY)

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_id = None
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_heartbeat(self):
        while True:
            try:
                self.client.send(cipher.encrypt("HEARTBEAT".encode(FORMAT)))
                time.sleep(HEARTBEAT_INTERVAL - 10)
            except Exception as e:
                print(f"Error in sending heartbeat: {e}")
                break

    def connect_client(self):
        self.client.connect((self.host, self.port))
        encrypted_client_id = self.client.recv(4096)
        self.client_id = cipher.decrypt(encrypted_client_id).decode(FORMAT)
        print(f"Client connected with ID: {self.client_id}")

        heartbeat_thread = threading.Thread(target=self.send_heartbeat)
        heartbeat_thread.daemon = True
        heartbeat_thread.start()

    @staticmethod
    def recvall(sock, buffer_size=4096):
        received_data = b""
        while True:
            chunk = sock.recv(buffer_size)
            if not chunk:
                break
            received_data += chunk
            dec_received_data = decrypt_data(received_data, cipher)
            if dec_received_data.endswith(b"<EnD>"):
                return dec_received_data[:-len(b"<EnD>")]

    def ask_query(self, query):
        if not self.client:
            raise ConnectionError("Client is not connected to the server.")
        encrypted_query = encrypt_data(query.encode(FORMAT), cipher)
        self.client.send(encrypted_query)
        decrypted_data = self.recvall(self.client)
        data = pickle.loads(decrypted_data)
        return data

    def close_client(self):
        if self.client:
            self.client.close()

from server import *

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 5000
    db_host = "localhost"
    db_user = "root"
    db_pswd = "@1234"
    db_name = "test"

    # Create server instance
    server = Server(server_host, server_port, db_host, db_user, db_pswd, db_name)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_server()
        print("Server stopped manually.")

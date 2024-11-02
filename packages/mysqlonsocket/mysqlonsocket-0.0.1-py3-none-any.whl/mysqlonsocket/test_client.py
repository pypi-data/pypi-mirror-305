from client import *

if __name__ == "__main__":
    # Default client settings (can be modified as needed)
    server_host = "127.0.0.1"
    server_port = 5000

    # Initialize and connect client
    client = Client(server_host, server_port)
    client.connect_client()

    # Example query (this can be expanded or replaced)
    # try:
    query = "SELECT * FROM t1;"
    result = client.ask_query(query)
    print("Query result:", result)
    # except Exception as e:
    #     print("Error:", e)
    # finally:
    #     client.close_client()

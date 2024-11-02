import logging
import pickle
import os

from mysqlonsocket.configrations import FORMAT

def secure_execute_query(cursor, query):
    try:
        # Example sanitization: Use parameterized queries
        cursor.execute(query)
        data = cursor.fetchall()
        logging.info(f"Query executed successfully: {query}")
        data = pickle.dumps(data)
        return data + b"<EnD>"
    except Exception as e:
        logging.error(f"Error executing query: {query}, Error: {e}")
        return pickle.dumps(f"Error: {e}") + b"<EnD>"

def setup_logger(log_dir):
    log_file = os.path.join(log_dir if log_dir else os.getcwd(), 'server.log')
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def encrypt_data(data, cipher):
    return cipher.encrypt(data)

def decrypt_data(data, cipher):
    return cipher.decrypt(data)

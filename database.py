import mysql.connector
from urllib.parse import urlparse

class Database(object):

    def __init__(self, conf):
        conn = None
        try:
            conn = mysql.connector.connect(**conf)
        except Exception as e:
            print(e)
        self.conn = conn
        self.cursor = conn.cursor()

    def get_cursor(self):
        return self.cursor
        
    def close(self):
        self.cursor.close()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
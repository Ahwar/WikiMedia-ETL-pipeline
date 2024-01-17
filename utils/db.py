import psycopg2
from psycopg2 import OperationalError


import logging
import sys


class PostGreSQL:
    def __init__(self):
        self.conn = None

    def connect(self, db_config):
        try:
            self.conn = psycopg2.connect(
                database=db_config.get("database"),
                user=db_config.get("user"),
                password=db_config.get("password"),
                host=db_config.get("host"),
                port=db_config.get("port"),
            )
        except OperationalError as e:
            logging.error(f"Error occurred while Connecting to PostgreSQL DB: {e}")
            sys.exit(1)

    def close(self):
        self.conn.close()

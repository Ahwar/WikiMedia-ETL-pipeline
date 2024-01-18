import psycopg2
from psycopg2 import OperationalError


import logging
import sys


class PostGreSQL:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self, db_config):
            """
            Connects to the PostgreSQL database using the provided configuration.

            Args:
                db_config (dict): A dictionary containing the database configuration parameters.

            Raises:
                OperationalError: If an error occurs while connecting to the database.

            Returns:
                None
            """
            try:
                self.conn = psycopg2.connect(
                    database=db_config.get("database"),
                    user=db_config.get("user"),
                    password=db_config.get("password"),
                    host=db_config.get("host"),
                    port=db_config.get("port"),
                )
                self.cursor = self.conn.cursor()
            except OperationalError as e:
                logging.error(f"Error occurred while Connecting to PostgreSQL DB: {e}")
                sys.exit(1)

    def close(self):
        self.conn.close()
        self.cursor.close()

    def table_exists(self, table_name):
        query = """
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE  table_name = %s
            )
        """
        self.cursor.execute(query, (table_name,))
        return self.cursor.fetchone()[0]

    def create_table_if_not_exists(self, table_name):
        if self.table_exists(table_name):
            logging.info(f"Table {table_name} already exists")

        else:
            logging.info(f"Creating table {table_name}")
            query = f"""
                    CREATE TABLE {table_name} (
                    referrer VARCHAR(255),
                    resource VARCHAR(255),
                    link_type VARCHAR(255),
                    count INT,
                    lang VARCHAR(255),
                    month VARCHAR(255)
                )
            """
            self.execute(query)
            logging.info(f"Table {table_name} created successfully")

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetch(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # function to loop over dataframe and insert each row to table
    def insert(self, df, table_name):
        """ Insert DataFrame data into table"""
        logging.info(f"Loading data to table {table_name}")
        query = f"""
            INSERT INTO {table_name} (referrer, resource, link_type, count, lang, month)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = df[['referrer', 'resource', 'link_type', 'count', 'lang', 'month']].values.tolist()
        self.cursor.executemany(query, values)
        self.conn.commit()
        logging.info(f"Loaded data to table {table_name} successfully")
    
    def get_distinct_list(self, column, table_name):
        """ Get distinct list of values from a column in a table """
        query = f"""
            SELECT DISTINCT {column} FROM {table_name}
        """
        return [lang[0] for lang in self.fetch(query)] 

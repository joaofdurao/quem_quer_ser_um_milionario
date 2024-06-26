"""
This script connects to MariaDB Platform and creates a cursor object.
"""
import sys
import mariadb


class CursorMariaDB:
    """
    A class representing a cursor object for MariaDB Platform.
    
    Attributes:
        DB_USER (str): The username for the database.
        DB_USER_PASSWD (str): The password for the database user.
        DB_HOST (str): The host address of the database.
        DB_PORT (int): The port number of the database.
        DB_SCHEMA (str): The name of the database schema.
        
    Methods:
        __init__(): Initializes the CursorMariaDB object and creates a connection and cursor 
        to the MariaDB Platform.
        create_connect(): Creates a connection and cursor object to the MariaDB Platform.
    """
    
    DB_USER = "root"
    DB_USER_PASSWD = "qwerty@123"
    DB_HOST = "localhost"
    DB_PORT = 3306
    DB_SCHEMA = "qsm_db"


    def create_connection(self):
        """
        Create a connection and a cursor object to MariaDB Platform.
        
        Args:
            db_user (str): The username for the database.
            db_password (str): The password for the database user.
            db_host (str): The host address of the database.
            db_port (int): The port number of the database.
            db_schema (str): The name of the database schema.
        
        Returns:
            conn (connection): The connection object for the MariaDB connection.
            cur (cursor): The cursor object for the MariaDB connection.
        """
        # Connect to MariaDB Platform
        try:
            conn = mariadb.connect(
                user = self.DB_USER,
                password = self.DB_USER_PASSWD,
                host = self.DB_HOST,
                port = self.DB_PORT,
                database = self.DB_SCHEMA
            )
            print("Connected to MariaDB Platform!")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # Get Cursor
        cur = conn.cursor()
        return conn, cur
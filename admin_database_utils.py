import mysql.connector
import os
class AdminDatabaseUtils:
   
    connection = None
    def __init__(self, connection = None):
        db_user = os.environ.get('CLOUD_SQL_USERNAME')
        db_password = os.environ.get('CLOUD_SQL_PASSWORD')
        db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
        db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
        if os.environ.get('GAE_ENV') == 'standard':
        # If deployed, use the local socket interface for accessing Cloud SQL
            unix_socket = '/cloudsql/{}'.format(db_connection_name)
            connection = mysql.connector.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
        else:
        # If running locally, use the TCP connections instead
        # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
        # so that your application can use 127.0.0.1:3306 to connect to your
        # Cloud SQL instance
            HOST = "127.0.0.1"
            USER = "root"
            PASSWORD = ""
            DATABASE = "Data"
            connection = mysql.connector.connect(user=USER, password=PASSWORD,
                              host=HOST, db=DATABASE)
        
        self.connection = connection
    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def deleteTable(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            drop table if exists Admins 
                """)
        self.connection.commit()

    def createAdminTable(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Admins (
                    admin_id int not null auto_increment,
                    username text not null,
                    password text not null,
                    constraint PK_Admins primary key (admin_id)
                )""")
        self.connection.commit()

    def insertAdmin(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute("insert into Admins (username, password) values (%s, %s)", (username, password,))
            
        self.connection.commit()

        return cursor.rowcount == 1
    
    def getAllAdmins(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from Admins")
        return cursor.fetchall()

    
import mysql.connector
import os
class LicenseDatabaseUtils:
   
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
            drop table if exists Licenses 
                """)
        self.connection.commit()


    def createLicenseTable(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Licenses (
                    license_id int not null auto_increment,
                    cust_id int not null,
                    license_num text not null,
                    country text not null,
                    state text not null,
                    issue_date date not null, 
                    expiry_date date not null, 
                    constraint PK_License primary key (license_id)
                )""")
        self.connection.commit()

    def insertLicenses(self, cust_id, license_num , country, state, issue_date, expiry_date):
        cursor = self.connection.cursor()
        cursor.execute("insert into Licenses (cust_id, license_num , country, state, issue_date, expiry_date) values (%s, %s, %s, %s, %s, %s)", (cust_id, license_num , country, state, issue_date, expiry_date,))
            
        self.connection.commit()

        return cursor.rowcount == 1
    
    def getAllLicenses(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from Licenses")
        return cursor.fetchall()

    def getCustomerLicense(self, cust_id):
        cursor = self.connection.cursor()
        cursor.execute("select * from Licenses where cust_id = %s", (cust_id,))
        return cursor.fetchall()

    def deleteLicense(self, license_num):
        cursor = self.connection.cursor()
        cursor.execute("delete from Licenses where license_num = %s", (license_num,))
        self.connection.commit()
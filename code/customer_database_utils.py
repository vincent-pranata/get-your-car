import mysql.connector
import os
class CustomerDatabaseUtils:
   
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
            drop table if exists Customers 
                """)
        self.connection.commit()


    def createCustomerTable(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Customers (
                    cust_id int not null auto_increment,
                    fname text not null,
                    lname text not null,
                    dob date not null, 
                    email text not null,
                    password text not null,
                    phone text not null,
                    plan int not null,
                    premium_expiry date,
                    constraint PK_Customer primary key (cust_id)
                )""")
        self.connection.commit()

    def insertCustomer(self, fname, lname, dob, email, password, phone, plan):
        cursor = self.connection.cursor()
        cursor.execute("insert into Customers (fname, lname, dob, email, password, phone, plan) values (%s, %s, %s, %s, %s, %s, %s)", (fname, lname, dob, email, password,phone, plan,))
            
        self.connection.commit()

        return cursor.rowcount == 1

    def insertDummy(self, fname, lname, dob, email, password, phone, plan, expiry):
        cursor = self.connection.cursor()
        cursor.execute("insert into Customers (fname, lname, dob, email, password, phone, plan, premium_expiry) values (%s, %s, %s, %s, %s, %s, %s,%s)", (fname, lname, dob, email, password,phone, plan,expiry,))
            
        self.connection.commit()

        return cursor.rowcount == 1

    def getAllCustomers(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from Customers")
        return cursor.fetchall()

    def getCustomer(self, email):
        cursor = self.connection.cursor()
        cursor.execute("select * from Customers WHERE email like %s", (email,))
        return cursor.fetchall()

    def resetPassword(self, password, cust_id):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Customers SET password = %s WHERE cust_id = %s", (password, cust_id,))
        self.connection.commit()

    def set_plan_standard(self,cust_id):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Customers SET plan = 0 WHERE cust_id = %s", (cust_id,))
        self.connection.commit()

    def set_plan_premium(self,cust_id):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Customers SET plan = 1 WHERE cust_id = %s", (cust_id,))
        self.connection.commit()

    def set_premium_expiry(self,date ,cust_id):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Customers SET premium_expiry = %s WHERE cust_id = %s", (date, cust_id,))
        self.connection.commit()


    def deleteCustomer(self, cust_id):
        cursor = self.connection.cursor()
        cursor.execute("delete from Customers where cust_id = %s", (cust_id,))
        self.connection.commit()
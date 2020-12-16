import mysql.connector
import os
class BookingDatabaseUtils:
   
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
            drop table if exists Bookings 
                """)
        self.connection.commit()


    def createBookingTable(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Bookings (
                    booking_id int not null auto_increment,
                    cust_id int not null,
                    car_id int not null,
                    start_date date not null,
                    start_time time not null,
                    end_date date not null, 
                    end_time time not null,
                    total_time time not null,
                    total_cost float not null,
                    status int not null,
                    constraint PK_Bookings primary key (booking_id)
                )""")
        self.connection.commit()

    def insertBooking(self, cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status):
        cursor = self.connection.cursor()
        cursor.execute("insert into Bookings (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status,))
            
        self.connection.commit()

        return cursor.rowcount == 1

    def getBooking(self, booking_id):
        cursor = self.connection.cursor()
        cursor.execute("select * from Bookings where booking_id = %s", (booking_id,))
        return cursor.fetchall()


    def getPersonalOngingBooking(self, cust_id):
        cursor = self.connection.cursor()
        cursor.execute("select * from Bookings where cust_id = %s and status=0", (cust_id,))
        return cursor.fetchall()

    def getPersonalBookingHistory(self, cust_id):
        cursor = self.connection.cursor()
        cursor.execute("select * from Bookings where cust_id = %s", (cust_id,))
        return cursor.fetchall()

    def updateStatus(self, status, booking_id):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Bookings SET status = %s WHERE booking_id = %s", (status, booking_id,))
        self.connection.commit()

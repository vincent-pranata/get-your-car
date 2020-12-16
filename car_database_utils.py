import mysql.connector
import os
class CarDatabaseUtils:
   
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
            drop table if exists Cars 
                """)
        self.connection.commit()


    def createCarTable(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Cars (
                    car_id int not null auto_increment,
                    name text not null,
                    colour text not null,
                    description text not null,
                    capacity int not null,
                    registration_plate text not null,
                    fuel_type int not null,
                    transmission int not null,
                    type text not null,
                    status int not null,
                    price int not null,
                    longitude float not null,
                    latitude float not null,
                    image text not null,
                    constraint PK_Cars primary key (car_id)
                )""")
        self.connection.commit()

    def insertCar(self, name, colour, description, capacity, registration_plate , fuel_type, transmission, type_, status, price, longitude, latitude, image):
        cursor = self.connection.cursor()
        cursor.execute("insert into Cars (name, colour, description, capacity , registration_plate , fuel_type, transmission, type, status, price, longitude, latitude, image) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, colour, description, capacity , registration_plate , fuel_type, transmission, type_, status, price, longitude, latitude,image,))
            
        self.connection.commit()

        return cursor.rowcount == 1
    
    def editCar(self, car_id, name, colour, description, capacity, registration_plate , fuel_type, transmission, type_, price, longitude, latitude, image):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Cars SET name = %s, colour = %s, description = %s, capacity = %s , registration_plate = %s, fuel_type = %s, transmission = %s, type = %s, price = %s, longitude = %s, latitude = %s, image = %s where car_id = %s", (name, colour, description, capacity , registration_plate , fuel_type, transmission, type_, price, longitude, latitude, image, car_id,))
            
        self.connection.commit()

        return cursor.rowcount == 1
    

    def getAllCars(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from Cars")
        return cursor.fetchall()

    def getAllAvalaibleCars(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from Cars where status = 0")
        return cursor.fetchall()

    def getAllCarExceptId(self, car_id):
        cursor = self.connection.cursor()
        cursor.execute("select * from Cars WHERE car_id != %s", (car_id,))
        return cursor.fetchall()

    def getCar(self, car_id):
        cursor = self.connection.cursor()
        cursor.execute("select * from Cars WHERE car_id = %s", (car_id,))
        return cursor.fetchall()

    def updateStatus(self, status, car_id):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Cars SET status = %s WHERE car_id = %s", (status, car_id,))
        self.connection.commit()

    def deleteCar(self, car_id):
        cursor = self.connection.cursor()
        cursor.execute("delete from Cars WHERE car_id = %s", (car_id,))
        self.connection.commit()

    def searchCarsName(self, search):
        cursor = self.connection.cursor()
        cursor.execute("select * from Cars WHERE lower(name) like %s and status = 0", ('%'+search+'%',))
        return cursor.fetchall()

    def searchCarsColour(self, search):
        cursor = self.connection.cursor()
        cursor.execute("select * from Cars WHERE lower(colour) like %s and status = 0", ('%'+search+'%',))
        return cursor.fetchall()

    def searchCarsTransmission(self, search):
        cursor = self.connection.cursor()
        cursor.execute("select * from Cars WHERE lower(transmission) like %s and status = 0", ('%'+search+'%',))
        return cursor.fetchall()

    def searchCarsType(self, search):
        cursor = self.connection.cursor()
        cursor.execute("select * from Cars WHERE lower(type) like %s and status = 0", ('%'+search+'%',))
        return cursor.fetchall()

    def searchCarsFuel(self, search):
        cursor = self.connection.cursor()
        cursor.execute("select * from Cars WHERE lower(fuel_type) like %s and status = 0", ('%'+search+'%',))
        return cursor.fetchall()

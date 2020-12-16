from customer_database_utils import CustomerDatabaseUtils
from admin_database_utils import AdminDatabaseUtils
from address_database_utils import AddressDatabaseUtils
from license_database_utils import LicenseDatabaseUtils
from car_database_utils import CarDatabaseUtils
from booking_database_utils import BookingDatabaseUtils
import hashlib, binascii, os, requests
from datetime import date, datetime

class Dummy:
    def __init__(self):
        self.createCustomerTable()
        self.createAdminTable()
        self.createAddressTable()
        self.createLicenseTable()
        self.createCarTable()
        self.createBookingTable()
        
    def createCustomerTable(self):
        with CustomerDatabaseUtils() as db:
            db.deleteTable()
            db.createCustomerTable()

    def createAdminTable(self):
        with AdminDatabaseUtils() as db:
            db.deleteTable()
            db.createAdminTable()

    def createAddressTable(self):
        with AddressDatabaseUtils() as db:
            db.deleteTable()
            db.createAddressTable()

    def createLicenseTable(self):
        with LicenseDatabaseUtils() as db:
            db.deleteTable()
            db.createLicenseTable()

    def createCarTable(self):
        with CarDatabaseUtils() as db:
            db.deleteTable()
            db.createCarTable()

    def createBookingTable(self):
        with BookingDatabaseUtils() as db:
            db.deleteTable()
            db.createBookingTable()

    def regularCarPrice(self, capacity, fuel_type, transmission):
        total = 30 + (capacity-2) + (fuel_type) + (transmission*5) 
        return total

    def getTotalBookingTime(self, start_date, start_time, end_date, end_time):
        import datetime as dtime
        sdate_obj = datetime.strptime(start_date, '%Y-%m-%d')
        edate_obj = datetime.strptime(end_date, '%Y-%m-%d')
        stime_obj = datetime.strptime(start_time, '%H:%M')
        etime_obj = datetime.strptime(end_time, '%H:%M')
        s_date_time = dtime.datetime.combine(sdate_obj, stime_obj.time())
        e_date_time = dtime.datetime.combine(edate_obj, etime_obj.time())
        date_time_difference = e_date_time - s_date_time
        total_hours = date_time_difference.total_seconds()/3600
        import math  
        hours = math.floor(total_hours)
        minutes_in_hours = total_hours - hours
        minutes = math.floor(minutes_in_hours*60)
        string_time = ""
        if minutes < 10:
            string_time = str(hours) + ":0" + str(minutes)
        else:
            string_time = str(hours) + ":" + str(minutes)
        return string_time
    
    def getTotalBookingCost(self, start_date, start_time, end_date, end_time, price):
        import datetime as dtime
        sdate_obj = datetime.strptime(start_date, '%Y-%m-%d')
        edate_obj = datetime.strptime(end_date, '%Y-%m-%d')
        stime_obj = datetime.strptime(start_time, '%H:%M')
        etime_obj = datetime.strptime(end_time, '%H:%M')
        s_date_time = dtime.datetime.combine(sdate_obj, stime_obj.time())
        e_date_time = dtime.datetime.combine(edate_obj, etime_obj.time())
        date_time_difference = e_date_time - s_date_time
        total_hours = date_time_difference.total_seconds()/3600
        total_cost = total_hours*price
        total_cost = round(total_cost, 2)
        return total_cost

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        passwordhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        passwordhash = binascii.hexlify(passwordhash)
        return (salt + passwordhash).decode('ascii')

    def insertCustomer(self, fname, lastname, dob, email, password, phone, plan, expiry):
        with CustomerDatabaseUtils() as db:
            db.insertDummy(fname, lastname, dob, email, self.hash_password(password), phone, plan, expiry)

    def insertLicense(self, cust_id, license_num, country, state, issue_date, expiry_date):
        with LicenseDatabaseUtils() as db:
            db.insertLicenses(cust_id, license_num, country, state, issue_date, expiry_date)

    def insertAddress(self, cust_id, unit_no, street, suburb, state, postcode):
        with AddressDatabaseUtils() as db:
            string_address = state + ", " + postcode
            url = 'https://maps.googleapis.com/maps/api/geocode/json'
            params = {'sensor': 'false', 'address': string_address, 'key': 'AIzaSyApAUIt3LozCwUFBGJY3F75w6U6IcLO_Ek'}
            r = requests.get(url, params=params)
            results = r.json()['results']
            location = results[0]['geometry']['location']                    
            db.insertAddress(cust_id, unit_no, street, suburb, state, postcode, location['lat'], location['lng'])

    def insertCar(self, name, colour, description, capacity , registration_plate, fuel_type, transmission, type_, status, longitude, latitude, image):
        with CarDatabaseUtils() as db:
            db.insertCar(name, colour, description, capacity , registration_plate , fuel_type, transmission, type_, status, self.regularCarPrice(capacity, fuel_type, transmission), longitude, latitude, image)
    
    def insertBooking(self, cust_id, car_id, start_date, start_time, end_date, end_time, price, status):
        with BookingDatabaseUtils() as db:
            db.insertBooking(cust_id, car_id, start_date, start_time, end_date, end_time, self.getTotalBookingTime(start_date, start_time, end_date, end_time), self.getTotalBookingCost(start_date, start_time, end_date, end_time, price), status)

    def insertAdmin(self, username, password):
        with AdminDatabaseUtils() as db:
            db.insertAdmin(username, self.hash_password(password))

    def dummy_cust(self):
        self.insertCustomer("Vincent","Pranata","1999-12-28","test@1234.com","1234",123456789,0, None)
        self.insertCustomer("Jerald","Tienzo","1999-01-02","test@1111.com","1234",123456789,1, "2020-10-20")
        self.insertCustomer("Youxin","Zheng","1999-01-01","test@2222.com","1234",123456789,0, "2020-10-12")
        self.insertCustomer("Yanfang","He","1999-01-03","test@3333.com","1234",123456789,1, "2020-11-10")
        self.insertCustomer("Test","123","1991-11-28","test@4444.com","1234",123456789,0, None)
        self.insertCustomer("Jerald","Tienzo","1994-03-01","test@5555.com","1234",123456789,1, "2020-11-20")
        self.insertCustomer("Youxin","Zheng","1995-02-02","test@6666.com","1234",123456789,0, "2020-12-12")
        self.insertCustomer("Yanfang","He","1997-11-03","test@7777.com","1234",123456789,0, None)
        self.insertCustomer("Vincent","Pranata","1998-11-28","test@8888.com","1234",123456789,0, None)
        self.insertCustomer("Jerald","Tienzo","2000-11-21","test@9999.com","1234",123456789, 0, None)
        
    def dummy_license(self):
        self.insertLicense(1, "abcd1234","Australia","VIC","2015-12-01", "2020-12-01")
        self.insertLicense(2, "aaaaaaaa","Australia","VIC","2015-12-02", "2020-12-02")
        self.insertLicense(3, "11111111","Australia","VIC","2015-12-03", "2020-12-03")
        self.insertLicense(4, "bbbbbbbb","Australia","VIC","2015-12-04", "2020-12-04")
        self.insertLicense(5, "abcd1234","Australia","VIC","2015-12-01", "2020-12-05")
        self.insertLicense(6, "cccccccc","Australia","VIC","2015-12-02", "2020-12-06")
        self.insertLicense(7, "22222222","Australia","VIC","2015-12-03", "2020-12-07")
        self.insertLicense(8, "33333333","Australia","VIC","2015-12-04", "2020-12-08")
        self.insertLicense(9, "dddddddd","Australia","VIC","2015-12-03", "2020-12-09")
        self.insertLicense(10, "xxxx1111","Australia","VIC","2015-12-04", "2020-12-10")

    def dummy_address(self):
        self.insertAddress(1, 101,"1st Avenue","Melbourne CBD","VIC", "3000")
        self.insertAddress(2, 102,"1st Avenue","Melbourne CBD","VIC", "3000")
        self.insertAddress(3, 103,"1st Avenue","Melbourne CBD","VIC", "3000")
        self.insertAddress(4, 104,"1st Avenue","Melbourne CBD","VIC", "3000")
        self.insertAddress(5, 201,"Russel Lane","Docklands","VIC", "3008")
        self.insertAddress(6, 202,"Queens Street","Hawthorn","VIC", "3122")
        self.insertAddress(7, 203,"King Road","Kew","VIC", "3101")
        self.insertAddress(8, 204,"Rose Avenue","Camberwell","VIC", "3124")
        self.insertAddress(9, 301,"Lily Road","South Yarra","VIC", "3141")
        self.insertAddress(10, 302,"3rd Avenue","Melbourne CBD","VIC", "3000")

    def dummy_booking(self):
        self.insertBooking(1, 1, "2020-12-29","15:55", "2020-12-30", "15:55", 35, 1)
        self.insertBooking(1, 8, "2020-01-09","15:55", "2020-01-10", "15:55", 30, 2)
        self.insertBooking(1, 9, "2020-08-09","15:55", "2020-08-10", "15:55", 41, 0)
        self.insertBooking(2, 7, "2020-09-09","15:55", "2020-09-10", "15:55", 34, 2)
        self.insertBooking(2, 9, "2020-12-29","15:25", "2020-12-30", "15:55", 35, 2)
        self.insertBooking(2, 1, "2020-12-29","15:25", "2020-12-30", "15:55", 35, 1)
        self.insertBooking(3, 2, "2020-12-29","15:15", "2020-12-29", "16:15", 32, 0)
        self.insertBooking(3, 3, "2020-12-29","15:15", "2020-12-29", "16:15", 32, 1)
        self.insertBooking(4, 4, "2020-12-28","15:05", "2020-12-28", "18:55", 37, 2)
        self.insertBooking(4, 5, "2020-12-28","15:05", "2020-12-28", "18:55", 37, 0)

    def dummy_car(self):
        self.insertCar("Alfa Romeo Spider","Mettalic Red", "bla bla bla bla", 2, "aaa111", 0, 1, "Coupe", 0, 144.664, -37.6152, "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRxKXtjfw7J1wKPnUkDd8WsnPSjpiS6nvEV1w&usqp=CAU")
        self.insertCar("Roll Royce Phantom","Black", "bla bla bla bla", 5, "fe1b12", 4, 0, "Sedan", 1, 144.364, -37.8152, "https://d3e706rdykep76.cloudfront.net/wp-content/uploads/sites/2/2016/10/RollsRoycePhantomBlackFront-1.jpg")
        self.insertCar("Bentley Bentayga","Blue", "bla bla bla bla", 5, "wef231", 3, 1, "Sedan", 0, 144.964, -37.8152, "https://cdn.motor1.com/images/mgl/6W7vX/s1/bentley-bentayga-design-series.jpg")
        self.insertCar("Lambhorgini Vintage","Yellow", "bla bla bla bla", 2, "a1rf51", 2, 0, "Coupe", 1, 144.764, -37.8152, "https://www.wired.com/images_blogs/autopia/2010/09/lamborghini-miura-sv-01.jpg")
        self.insertCar("Pajero Sport","Blue", "bla bla bla bla", 6, "aef231", 3, 1, "SUV", 1, 144.964, -37.8102, "https://motoring.pxcrush.net/motoring/general/editorial/mitsubishi-pajero-sport-154.jpg?width=1024")
        self.insertCar("Ferrari la Ferrari","Red", "bla bla bla bla", 2, "awhf51", 4, 1, "Coupe", 1, 144.764, -37.8102, "https://api.ferrarinetwork.ferrari.com/v2/network-content/medias/resize/5ddb97392cdb32285a799dfa-laferrari-2013-share?apikey=9QscUiwr5n0NhOuQb463QEKghPrVlpaF&width=1080")
        self.insertCar("Porsche 911","Black", "bla bla bla bla", 2, "gu4332", 2, 1, "Coupe", 0, 144.954, -37.8102, "https://newsroom.porsche.com/.imaging/mte/porsche-templating-theme/image_1080x624/dam/porsche_newsroom/Produkte/911/911-Carrera-Black-Edition/P15_0437_a4_rgb/jcr:content/Black-Edition-3300x1860-MS-mittig.jpg")
        self.insertCar("MINI Cooper","Brown", "bla bla bla bla", 5, "ibe21", 1, 0, "Hatchback", 0, 144.634, -37.8150, "https://i.pinimg.com/originals/f7/7f/80/f77f806b88112c65088ad3ecf17a231a.jpg")
        self.insertCar("Honda Civic","Silver", "bla bla bla bla", 5, "fwhuf", 2, 1, "Sedan", 0, 144.604, -37.8040, "https://media.caradvice.com.au/image/private/c_fill,q_auto,f_auto,w_400,ar_16:9/trnfkpxmizhxcaalmsj9.jpg")
        self.insertCar("BMW M5","Black", "bla bla bla bla", 5, "woeffoiw", 2, 1, "Saloon", 1, 144.624, -37.8120, "https://i.redd.it/2aciz8dn5ld31.jpg")

    def dummy_admin(self):
        self.insertAdmin("admin1","1111")
        self.insertAdmin("admin2","1111")
        self.insertAdmin("admin3","1111")
        self.insertAdmin("admin4","1111")
        self.insertAdmin("admin5","1111")
        self.insertAdmin("admin6","1111")
        self.insertAdmin("admin7","1111")
        self.insertAdmin("admin8","1111")
        self.insertAdmin("admin9","1111")
        self.insertAdmin("admin10","1111")

d = Dummy()
d.dummy_cust()
d.dummy_address()
d.dummy_admin()
d.dummy_car()
d.dummy_booking()
d.dummy_license()

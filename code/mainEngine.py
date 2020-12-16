import hashlib, binascii, os
from datetime import date, datetime
from customer_database_utils import CustomerDatabaseUtils
from admin_database_utils import AdminDatabaseUtils
from address_database_utils import AddressDatabaseUtils
from license_database_utils import LicenseDatabaseUtils
from car_database_utils import CarDatabaseUtils
from booking_database_utils import BookingDatabaseUtils

class MainEngine:
    def __init__(self):
        self.createCustomerTable()
        self.createAdminTable()
        self.createAddressTable()
        self.createLicenseTable()
        self.createCarTable()
        self.createBookingTable()
        
    def createCustomerTable(self):
        with CustomerDatabaseUtils() as db:
            db.createCustomerTable()

    def createAdminTable(self):
        with AdminDatabaseUtils() as db:
            db.createAdminTable()

    def createAddressTable(self):
        with AddressDatabaseUtils() as db:
            db.createAddressTable()

    def createLicenseTable(self):
        with LicenseDatabaseUtils() as db:
            db.createLicenseTable()

    def createCarTable(self):
        with CarDatabaseUtils() as db:
            db.createCarTable()

    def createBookingTable(self):
        with BookingDatabaseUtils() as db:
            db.createBookingTable()

    def login(self, email, password):
        find = False
        with CustomerDatabaseUtils() as db:
            for cust in db.getAllCustomers():
                find = False
                if cust[4]==email and self.verify_password(cust[5], password):
                    find = True
                    break
        return find

    def admin_login(self, username, password):
        find = False
        with AdminDatabaseUtils() as db:
            for admin in db.getAllAdmins():
                find = False
                if admin[1]==username and self.verify_password(admin[2], password):
                    find = True
                    break
        return find


    def register(self, fname, lastname, dob, email, password, phone):
        with CustomerDatabaseUtils() as db:
            db.insertCustomer(fname, lastname, dob, email, self.hash_password(password), phone, 0)

    def getCustomer(self, email):
        with CustomerDatabaseUtils() as db:
            for cust in db.getCustomer(email):
                return cust 
        return None

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        passwordhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        passwordhash = binascii.hexlify(passwordhash)
        return (salt + passwordhash).decode('ascii')

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                      provided_password.encode('utf-8'), 
                                      salt.encode('ascii'), 
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def check_duplicate_email(self, email):
        duplicate = False
        with CustomerDatabaseUtils() as db:
            for cust in db.getAllCustomers():
                if cust[4]==email:
                    duplicate = True
        return duplicate

    def insertLicense(self, cust_id, license_num, country, state, issue_date, expiry_date):
        with LicenseDatabaseUtils() as db:
            db.insertLicenses(cust_id, license_num, country, state, issue_date, expiry_date)

    def getLicense(self, cust_id):
        with LicenseDatabaseUtils() as db:
            for license in db.getCustomerLicense(cust_id):
                return license 
        return None

    def insertAddress(self, cust_id, unit_no, street, suburb, state, postcode, latitude, longitude):
        with AddressDatabaseUtils() as db:
            db.insertAddress(cust_id, unit_no, street, suburb, state, postcode, latitude, longitude)

    def getAddress(self, cust_id):
        with AddressDatabaseUtils() as db:
            for address in db.getCustomerAddress(cust_id):
                return address
        return None

    def validateDOB(self, dob):
        valid = False
        current_year = date.today().year
        
        dob_obj = datetime.strptime(dob, '%Y-%m-%d')
        age = current_year - dob_obj.year
        if age >= 18:
            valid = True
        return valid
    
    def validateLicenseDate(self, issue, expiry):
        import datetime as dtime
        valid = False
        today = datetime.today()
        issue_split = issue.split(sep = "-", maxsplit = 2)
        issue_obj = dtime.datetime(int(issue_split[0]), int(issue_split[1]), int(issue_split[2]))   
        
        expiry_split = expiry.split(sep = "-", maxsplit = 2)
        expiry_obj = dtime.datetime(int(expiry_split[0]), int(expiry_split[1]), int(expiry_split[2]))   
        if issue_obj < today and expiry_obj > issue_obj and expiry_obj > today:
            valid = True
        return valid

    def validateCustCredentials(self, email, fname, lname, dob):
        cust_id = None
        cust = self.getCustomer(email)
        if cust is not None:
            if email == cust[4] and fname.lower() == cust[1].lower() and lname.lower() == cust[2].lower() and dob == cust[3].strftime("%Y-%m-%d"):
                cust_id = cust[0]
        return cust_id

    def confirmPassword(self, password, confirm_password):
        if confirm_password == password:
            return True
        return False

    def resetPassword(self, password, cust_id):
        with CustomerDatabaseUtils() as db:
            db.resetPassword(self.hash_password(password), cust_id)

    def validateBookingTime(self, start_date, start_time, end_date, end_time):
        valid = False
        sdate_obj = datetime.strptime(start_date, '%Y-%m-%d')
        edate_obj = datetime.strptime(end_date, '%Y-%m-%d')
        today = datetime.today()
        today = today.replace(minute=00, hour=00, second=00, microsecond=000000)
        if sdate_obj >= today: 
            if sdate_obj < edate_obj:
                valid = True
            elif sdate_obj == edate_obj:
                stime_obj = datetime.strptime(start_time, '%H:%M')
                etime_obj = datetime.strptime(end_time, '%H:%M')
                if etime_obj > stime_obj:
                    valid = True

        return valid

    def insertCar(self, name, colour, description, capacity , registration_plate, fuel_type, transmission, type_, longitude, latitude, image):
        with CarDatabaseUtils() as db:
            db.insertCar(name, colour, description, capacity , registration_plate , fuel_type, transmission, type_, 0, self.regularCarPrice(capacity, fuel_type, transmission), longitude, latitude, image)
    
    def distance(self, car_list, address):
        import math
        cars = []
        lat2 = address[7]
        lon2 = address[8]
        for car in car_list:
            lat1 = car[12]
            lon1 = car[11]
            radius = 6371 # earth radius in km

            dlat = math.radians(lat2-lat1)
            dlon = math.radians(lon2-lon1)
            a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = radius * c
            print(d)
            if d <= 5:
                cars.append(car)
        return cars

    def carRegistrationValidation(self, registration_plate):
        valid = True
        cars = self.getAllCars()
        for car in cars:
            if car[5].lower() == registration_plate.lower():
                valid = False
                break
        return valid

    def editCar(self, car_id, name, colour, description, capacity , registration_plate, fuel_type, transmission, type_, longitude, latitude, image):
        with CarDatabaseUtils() as db:
            db.editCar(car_id, name, colour, description, capacity , registration_plate , fuel_type, transmission, type_,  self.regularCarPrice(capacity, fuel_type, transmission), longitude, latitude, image)

    def editCarRegistrationValidation(self, registration_plate, car_id):
        valid = True
        with CarDatabaseUtils() as db:
            cars = db.getAllCarExceptId(car_id)
            for car in cars:
                if car[5].lower() == registration_plate.lower():
                    valid = False
                    break
            return valid

    def regularCarPrice(self, capacity, fuel_type, transmission):
        total = 30 + (int(capacity)-2) + (int(fuel_type)) + (int(transmission)*5) 
        return total

    def getAllCustomers(self):
        with CustomerDatabaseUtils() as db:
            return db.getAllCustomers()

    def getAllLicenses(self):
        with LicenseDatabaseUtils() as db:
            return db.getAllLicenses()

    def getAllAddresses(self):
        with AddressDatabaseUtils() as db:
            return db.getAllAddresses()

    def getAllCars(self):
        with CarDatabaseUtils() as db:
            return db.getAllCars()
    
    def getAvalaibleCars(self):
        with CarDatabaseUtils() as db:
            return db.getAllAvalaibleCars()
    
    def setCarAvalaible(self, car_id):
        with CarDatabaseUtils() as db:
            db.updateStatus(0, car_id)

    def setCarUnavalaible(self, car_id):
        with CarDatabaseUtils() as db:
            db.updateStatus(1, car_id)

    def getCar(self, car_id):
        with CarDatabaseUtils() as db:
            return db.getCar(car_id)

    def deleteCar(self, car_id):
        with CarDatabaseUtils() as db:
            db.deleteCar(car_id)

    def makeBooking(self, cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost):
        with BookingDatabaseUtils() as db:
            db.insertBooking(cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, 0)

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

    def getPersonalOngoingBooking(self, cust_id):
        with BookingDatabaseUtils() as db:
            return db.getPersonalOngingBooking(cust_id)

    def getPersonalBookingHistory(self, cust_id):
        with BookingDatabaseUtils() as db:
            return db.getPersonalBookingHistory(cust_id)

    def searchCars(self, column, search):
        with CarDatabaseUtils() as db:
            if column == 'name':
                return db.searchCarsName(search)
            elif column == 'type':
                return db.searchCarsType(search)
            elif column == 'colour':
                return db.searchCarsColour(search)
            elif column == 'fuel_type':
                return db.searchCarsFuel(search)
            elif column == 'transmission':
                return db.searchCarsTransmission(search)

    def set_plan(self, plan, cust_id):
        with CustomerDatabaseUtils() as db:
            if plan == 0:
                db.set_plan_premium(cust_id)
            else:
                db.set_plan_standard(cust_id)

    def validate_premium(self, date_):
        valid = False
        today = date.today()
        if date_ >= today:
            valid = True
        return valid 

    def cancelBooking(self, booking_id):
        with BookingDatabaseUtils() as db:
            db.updateStatus(2, booking_id)

    def completeBooking(self, booking_id):
        with BookingDatabaseUtils() as db:
            db.updateStatus(1, booking_id)

    def getBooking(self, booking_id):
        with BookingDatabaseUtils() as db:
            return db.getBooking(booking_id)

    def set_premium_expiry(self, cust_id):
        with CustomerDatabaseUtils() as db:
            today = date.today()
            from datetime import timedelta
            today = today + timedelta(days=30)
            return db.set_premium_expiry(today, cust_id)

    def card_validation(self, card_name, card_num, date, cvv):
        valid = True
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        today = today.replace(minute=00, hour=00, second=00, microsecond=000000)
        if any(char.isdigit() for char in card_name) or len(card_num)!=16 or len(cvv)!=3 or date_obj<today:
            valid=False
        return valid


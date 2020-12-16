import unittest
from mainEngine import MainEngine

class MainEngineTest(unittest.TestCase):
    def setUp(self):
        self.mainEngine = MainEngine()
    
    def test_hash_successful(self):
        hashed = self.mainEngine.hash_password("1234")
        self.assertTrue(self.mainEngine.verify_password(hashed,"1234"))
    
    def test_hash_fail(self):
        hashed = self.mainEngine.hash_password("1233")
        self.assertFalse(self.mainEngine.verify_password(hashed,"1234"))
        
    def test_valid_DOB(self):
        dob = "1999-12-28"
        self.assertTrue(self.mainEngine.validateDOB(dob))

    def test_invalid_DOB(self):
        dob = "2012-12-28"
        self.assertFalse(self.mainEngine.validateDOB(dob))
            
    def test_valid_lincense_date(self):
        issue_date = "2018-12-10"
        expiry_date = "2021-12-10"
        self.assertTrue(self.mainEngine.validateLicenseDate(issue_date, expiry_date))
            
    def test_invalid_lincense_date(self):
        issue_date = "2012-12-10"
        expiry_date = "2015-12-10"
        self.assertFalse(self.mainEngine.validateLicenseDate(issue_date, expiry_date))
        issue_date = "2020-12-10"
        expiry_date = "2023-12-10"
        self.assertFalse(self.mainEngine.validateLicenseDate(issue_date, expiry_date))
        issue_date = "2023-12-10"
        expiry_date = "2020-12-10"
        self.assertFalse(self.mainEngine.validateLicenseDate(issue_date, expiry_date))

    def test_validate_booking_time_success(self):
        self.assertTrue(self.mainEngine.validateBookingTime("2020-12-11", "14:00","2020-12-12", "15:00"))    

    def test_validate_booking_time_fail(self):
        self.assertFalse(self.mainEngine.validateBookingTime("2020-09-01", "14:00", "2020-09-02", "15:00"))    

    def test_validate_customer_credentials_success(self):
        self.assertEqual(self.mainEngine.validateCustCredentials("test@1234.com", "Vincent", "Pranata", "1999-12-28"), 1)

    def test_validate_customer_credentials_fail(self):
        self.assertEqual(self.mainEngine.validateCustCredentials("test@1234.com", "Vincent", "Pranafewa", "1999-12-28"), None)

    def test_car_registration_success(self):
        self.assertTrue(self.mainEngine.carRegistrationValidation("fewheuw1234"))

    def test_car_registration_fail(self):
        self.assertFalse(self.mainEngine.carRegistrationValidation("aaa111"))

    def test_login_success(self):
        self.assertTrue(self.mainEngine.login("test@1234.com","1234"))

    def test_login_fail(self):
        self.assertFalse(self.mainEngine.login("test@1234.com","1233"))
        
    def test_register_success(self):
        self.assertFalse(self.mainEngine.check_duplicate_email("aqwguei@gmail.com"))
    
    def test_register_fail(self):
        self.assertTrue(self.mainEngine.check_duplicate_email("test@1234.com"))

    def test_card_validation_success(self):
        name = "Vincent Pranata"
        card = "1111111111111111"
        date = "2023-12-10"
        cvv = "123"
        self.assertTrue(self.mainEngine.card_validation(name, card, date, cvv))

    def test_card_validation_fail(self):
        name1 = "V1ncent"
        card1 = "1111111111111111"
        date1 = "2023-12-10"
        cvv1 = "123"
        self.assertFalse(self.mainEngine.card_validation(name1, card1, date1, cvv1))
        name2 = "Vincent"
        card2 = "111111111111111"
        date2 = "2023-12-10"
        cvv2 = "123"
        self.assertFalse(self.mainEngine.card_validation(name2, card2, date2, cvv2))
        name3 = "V1ncent"
        card3 = "1111111111111111"
        date3 = "2019-12-10"
        cvv3 = "123"
        self.assertFalse(self.mainEngine.card_validation(name3, card3, date3, cvv3))
        name4 = "Vincent"
        card4 = "1111111111111111"
        date4 = "2023-12-10"
        cvv4 = "12"
        self.assertFalse(self.mainEngine.card_validation(name4, card4, date4, cvv4))

    def test_calculate_total_booking_cost(self):
        start_date = "2020-12-10"
        start_time = "12:00"
        end_date = "2020-12-10"
        end_time = "15:00"
        price = 10
        self.assertEqual(self.mainEngine.getTotalBookingCost(start_date, start_time, end_date, end_time, price), 30)

    def test_calculate_total_booking_time(self):
        start_date = "2020-12-10"
        start_time = "12:00"
        end_date = "2020-12-10"
        end_time = "15:00"
        self.assertEqual(self.mainEngine.getTotalBookingTime(start_date, start_time, end_date, end_time), "3:00")

    def test_validate_premium_expiry_success(self):
        from datetime import date
        date_ = date.today()
        self.assertTrue(self.mainEngine.validate_premium(date_))        

    def test_validate_premium_expiry_fail(self):
        from datetime import date
        date_ = date.today()
        date_ = date_.replace(year=2019)
        self.assertFalse(self.mainEngine.validate_premium(date_))

    def test_calculate_car_price(self):
        # Capacity (INT) 
        # Standard Capacity = 2 
        
        # Fuel Type (INT) 
        # Standard Unleaded 91 (0) 
        # Premium 95-octane unleaded (1) 
        # Premium 98-octane unleaded (2) 
        # E10 (3) 
        # E85 (4) 
        
        # Transmission (INT) 
        # Auto = 1 
        # Manual = 0 
        
        capacity = 6
        fuel_type = 0
        transmission = 0
        self.assertEqual(self.mainEngine.regularCarPrice(capacity, fuel_type, transmission), 34)

        capacity = 4
        fuel_type = 3
        transmission = 1
        self.assertEqual(self.mainEngine.regularCarPrice(capacity, fuel_type, transmission), 40)

        capacity = 2
        fuel_type = 1
        transmission = 0
        self.assertEqual(self.mainEngine.regularCarPrice(capacity, fuel_type, transmission), 31)

    def test_find_customer_address_coordinates(self):
        import requests
        string_address = "3000, VIC"
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {'sensor': 'false', 'address': string_address, 'key': 'AIzaSyApAUIt3LozCwUFBGJY3F75w6U6IcLO_Ek'}
        r = requests.get(url, params=params)
        results = r.json()['results']
        location = results[0]['geometry']['location']      
        self.assertEqual(location['lat'], -37.8152065)
        self.assertEqual(location['lng'], 144.963937) 

        string_address = "3122, VIC"
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {'sensor': 'false', 'address': string_address, 'key': 'AIzaSyApAUIt3LozCwUFBGJY3F75w6U6IcLO_Ek'}
        r = requests.get(url, params=params)
        results = r.json()['results']
        location = results[0]['geometry']['location']      
        self.assertEqual(location['lat'], -37.8222114)
        self.assertEqual(location['lng'], 145.0328017) 

if __name__ == "__main__":
    unittest.main()

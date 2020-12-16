from flask import Flask, jsonify, render_template, request, redirect, session, url_for
import requests,os,json
from flask_googlemaps import Map
from flask_googlemaps import icons
from app import app, mainEngine, gMap

@app.route('/')
def index():
    return render_template("mainlogin.html")

@app.route('/login', methods = ('GET','POST'))
def login():
    error = False
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        error = True
        if mainEngine.login(email, password):
            session['email'] = email
            return redirect('/customer/home')            
    return render_template("index.html", error = error, success = False, change = False)

@app.route('/admin', methods = ('GET','POST'))
def adminlogin():
    error = False
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        error = True
        if mainEngine.admin_login(username, password):
            session['username'] = username
            return redirect('/admin/home')            
    return render_template("adminLogin.html", error = error)

@app.route('/admin/home')
def admin_home():
    return render_template("admin/home.html", username = session['username'] )

@app.route('/admin/carlist')
def admin_car():
    cars = mainEngine.getAllCars()
    return render_template("admin/carlist.html", cars = cars )

@app.route('/admin/addcar', methods = ('GET','POST'))
def addcar():
    success = True
    if request.method=='POST':
        name = request.form['name']
        colour = request.form['color']
        description = request.form['description'] 
        capacity = request.form['capacity']
        registration_plate = request.form['regPlate']
        fuel_type = request.form['fuel']
        transmission = request.form['transmission']
        type_ = request.form['type']
        image = request.form['image']
        longitude = request.form['longitude']
        latitude = request.form['latitude']
        if mainEngine.carRegistrationValidation(registration_plate):
            mainEngine.insertCar(name, colour, description, capacity, registration_plate, fuel_type, transmission, type_, longitude, latitude, image)             
            return redirect("/admin/carlist")
        success = False
    return render_template("admin/addcar.html", success = success)

@app.route('/admin/editcarpage', methods = ['POST'])
def updatecarpage():
    car_id = request.form['id']
    car = mainEngine.getCar(car_id)[0]
    return render_template('admin/editcar.html', car=car)

@app.route('/admin/edit-car', methods = ['POST'])
def editcar():
    success = True
    car_id = request.form['id']
    car = mainEngine.getCar(car_id)[0]
    name = request.form['name']
    colour = request.form['color']
    description = request.form['description'] 
    capacity = request.form['capacity']
    registration_plate = request.form['regPlate']
    fuel_type = request.form['fuel']
    transmission = request.form['transmission']
    type_ = request.form['type']
    image = request.form['image']
    longitude = request.form['longitude']
    latitude = request.form['latitude']
    if mainEngine.editCarRegistrationValidation(registration_plate, car_id):
        mainEngine.editCar(car_id, name, colour, description, capacity, registration_plate, fuel_type, transmission, type_, longitude, latitude, image)             
        return redirect("/admin/carlist")
    success = False
    return render_template("admin/editcar.html", car=car, success = success)


@app.route('/admin/userlist')
def userlist():
    customers = mainEngine.getAllCustomers()
    addresses = mainEngine.getAllAddresses()
    licenses = mainEngine.getAllLicenses()
    
    return render_template("admin/userlist.html", customers = customers, addresses = addresses, licenses = licenses)


@app.route('/register', methods = ('GET', 'POST'))
def register():
    error = False
    validDOB = True
    validLicense = True
    if request.method=='POST':
        # personal details
        fname = request.form['fname']
        lname = request.form['lname']
        dob = request.form['date']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        # address details 
        unit = request.form['unitno']
        street = request.form['street']
        suburb = request.form['suburb']
        state = request.form['state']
        postcode = request.form['postcode']
        
        string_address = postcode + ", " + state

        # license details
        lnumber = request.form['lnumber']
        country = request.form['country']
        license_state = request.form['license-state']
        issue_date = request.form['idate']
        expiry_date = request.form['edate']

        if mainEngine.check_duplicate_email(email) is False:
            if mainEngine.validateDOB(dob) is True:
                if mainEngine.validateLicenseDate(issue_date, expiry_date):
                    mainEngine.register(fname, lname, dob, email, password, phone)
                    cust_id = mainEngine.getCustomer(email)[0]
                    url = 'https://maps.googleapis.com/maps/api/geocode/json'
                    params = {'sensor': 'false', 'address': string_address, 'key': 'AIzaSyApAUIt3LozCwUFBGJY3F75w6U6IcLO_Ek'}
                    r = requests.get(url, params=params)
                    results = r.json()['results']
                    location = results[0]['geometry']['location']                    
                    mainEngine.insertAddress(cust_id, unit, street, suburb, state, postcode, location['lat'], location['lng'])
                    mainEngine.insertLicense(cust_id, lnumber, country, license_state, issue_date, expiry_date)
                    return render_template("index.html", error = False, success = True, change = False)
                else:
                    validLicense = False
            else:
                validDOB = False
        else:
            error = True
    return render_template("register.html", error = error, validDOB = validDOB, validLicense = validLicense)

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@app.route('/customer/home')
def home():
    return render_template("customer/home.html", email = session['email'])

@app.route('/customer/booking', methods = ('GET', 'POST'))
def booking():
    valid = True
    
    if request.method=='POST':
        car_id = request.form['car']
        start_date = request.form['sdate']
        start_time = request.form['stime']
        end_date = request.form['edate']
        end_time = request.form['etime']
        if mainEngine.validateBookingTime(start_date, start_time, end_date, end_time):
            time = mainEngine.getTotalBookingTime(start_date, start_time, end_date, end_time)
            cust = mainEngine.getCustomer(session['email'])
            plan = cust[7]
            cars = mainEngine.getCar(car_id)
            cost = 0
            if plan == 0:
                cost = mainEngine.getTotalBookingCost(start_date, start_time, end_date, end_time, cars[0][10])
            else:
                cost = mainEngine.getTotalBookingCost(start_date, start_time, end_date, end_time, 15)
            return render_template("customer/bookingPayment2.html", cars=cars, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, time=time, cost=cost, success=True)
        else:
            valid = False
    
    cars = mainEngine.getAvalaibleCars()
    mark = []
    if cars:
        for car in cars:
            mark.append((float(car[12]), float(car[11]), car[1]))

    gmap = Map(
        identifier="gmap",
        varname="gmap",
        #MELBOURNE COORDINATE
        lat=-37.8136,
        lng=144.9631,
        markers={
            icons.dots.blue: mark,
        },
        style="height:max-500px;max-width:1000px;margin:0;margin-left:auto;margin-right:auto;",
    )
    return render_template("customer/booking2.html", cars = cars, gmap = gmap, valid = valid)

@app.route('/customer/booking-summary', methods = ['POST'])
def booking_summary():
    if request.method=='POST':
        car_id = request.form['car']
        start_date = request.form['sdate']
        start_time = request.form['stime']
        end_date = request.form['edate']
        end_time = request.form['etime']
        time = request.form['time']
        cost = request.form['cost']

        name = request.form['namecard']
        card = request.form['cardnumber']
        date = request.form['date']
        cvv = request.form['cvv']
        cust = mainEngine.getCustomer(session['email'])
        if mainEngine.card_validation(name, card, date, cvv):
            mainEngine.makeBooking(cust[0], car_id, start_date, start_time, end_date, end_time, time, cost)
            mainEngine.setCarUnavalaible(car_id)
            return redirect("/customer/ongoing-booking")
        else:
            cars = mainEngine.getCar(car_id)
            return render_template("customer/bookingPayment2.html", cars=cars, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, time=time, cost=cost, success=False)
        
@app.route('/reset-password', methods = ('GET', 'POST'))
def reset():
    invalid = False
    diff = False
    if request.method=='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        dob = request.form['date']
        email = request.form['email']
        password = request.form['pass']
        confirm_password = request.form['cpass']
        cust_id = mainEngine.validateCustCredentials(email, fname, lname, dob)
        if cust_id is not None:
            if mainEngine.confirmPassword(password, confirm_password):
                mainEngine.resetPassword(password, cust_id)
                return render_template("index.html", error = False, success = False, change = True)
            else:
                diff = True
        else:
            invalid = True
    return render_template("reset-1.html", invalid = invalid, diff = diff)

@app.route('/customer/ongoing-booking')
def ongoing_booking():
    cust_id = mainEngine.getCustomer(session['email'])[0]
    bookings = mainEngine.getPersonalOngoingBooking(cust_id)
    cars = mainEngine.getAllCars()
    return render_template("customer/ongoingBooking.html", bookings = bookings, cars = cars)

@app.route('/customer/booking-history')
def booking_history():
    cust_id = mainEngine.getCustomer(session['email'])[0]
    bookings = mainEngine.getPersonalBookingHistory(cust_id)
    cars = mainEngine.getAllCars()
    return render_template("customer/bookingHistory.html", bookings = bookings, cars = cars)

@app.route('/customer/search-car', methods = ('GET', 'POST'))
def search_car():
    cars = {}
    if request.method=='POST':
        column = request.form['column']
        search = request.form['search']
        cars = mainEngine.searchCars(column, search)
    
    mark = []
    if cars:
        for car in cars:
            mark.append((float(car[12]), float(car[11]), car[1]))

    gmap = Map(
        identifier="gmap",
        varname="gmap",
        #MELBOURNE COORDINATE
        lat=-37.8136,
        lng=144.9631,
        markers={
            icons.dots.blue: mark,
        },
        style="height:max-500px;max-width:1000px;margin:0;margin-left:auto;margin-right:auto;",
    )
    
    return render_template("/customer/searchCar.html", gmap=gmap, cars= cars)

@app.route('/customer/search-car-near-me', methods = ['POST'])
def search_car_by_location():
    cust_id = mainEngine.getCustomer(session['email'])[0]
    address = mainEngine.getAddress(cust_id)
    car_list = mainEngine.getAvalaibleCars()
    cars = mainEngine.distance(car_list, address)
    mark = []
    if cars:
        for car in cars:
            mark.append((float(car[12]), float(car[11]), car[1]))

    gmap = Map(
        identifier="gmap",
        varname="gmap",
        #MELBOURNE COORDINATE
        lat=address[7],
        lng=address[8],
        markers={
            icons.dots.blue: mark,
        },
        style="height:max-500px;max-width:1000px;margin:0;margin-left:auto;margin-right:auto;",
    )
    
    return render_template("/customer/searchCar.html", gmap=gmap, cars= cars)

@app.route('/customer/plan')
def plan():
    cust = mainEngine.getCustomer(session['email'])
    plan = cust[7]
    return render_template("/customer/price.html", plan = plan)

@app.route('/customer/set-plan')
def set_standard():
    cust = mainEngine.getCustomer(session['email'])
    mainEngine.set_plan(cust[7],cust[0])
    return redirect("/customer/plan")

@app.route('/customer/cancel-booking', methods = ['POST'])
def cancel_booking():
    booking_id = request.form['booking_id']
    mainEngine.cancelBooking(booking_id)
    booking = mainEngine.getBooking(booking_id)
    mainEngine.setCarAvalaible(booking[0][2])
    return redirect("/customer/ongoing-booking")

@app.route('/customer/complete-booking', methods = ['POST'])
def complete_booking():
    booking_id = request.form['booking_id']
    mainEngine.completeBooking(booking_id)
    booking = mainEngine.getBooking(booking_id)
    mainEngine.setCarAvalaible(booking[0][2])
    return redirect("/customer/booking-history")

@app.route('/admin/delete-car', methods = ['POST'])
def delete_car():
    car_id = request.form['car_id']
    mainEngine.deleteCar(car_id)
    return redirect("/admin/carlist")

@app.route('/customer/plan-summary', methods = ('GET', 'POST'))
def plan_summary():
    cust = mainEngine.getCustomer(session['email'])
    if request.method=='POST':
        name = request.form['namecard']
        card = request.form['cardnumber']
        date = request.form['date']
        cvv = request.form['cvv']
        
        if mainEngine.card_validation(name, card, date, cvv):
            mainEngine.set_premium_expiry(cust[0])
        else:
            return render_template("customer/planPayment2.html", success=False)

    cust = mainEngine.getCustomer(session['email'])
    if not cust[8] or not mainEngine.validate_premium(cust[8]):
        return render_template("customer/planPayment2.html", success=True)

    return redirect("/customer/set-plan")
        

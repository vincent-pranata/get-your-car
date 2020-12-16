drop table if exists Admins;
create table if not exists Admins (
    admin_id int not null auto_increment,
    username text not null,
    password text not null,
    constraint PK_Admins primary key (admin_id)
);
insert into Admins (username, password) values ("admin1","f958f88c033ffa8ff2f2fab47d5c1aa25bacaf5df091630e54a4ec46eef9aeceef0bac88977d875aa11aaeb965ec834301f05c86a8fadb7f1614bb34772ddd1ad42a6fcc955c74747d9383e3e711f1d9848f1ec22dc949e91e6c49bc1c864532");
insert into Admins (username, password) values ("admin2","955c65d1f52370213049d02164d70c3cea197bc477bfa11bf996f2a802f7807152979443c7cc7ed88dad5bb24db812accbdf0c04fd3358b132dfb7d2a207f96e3779ae37a748e9f67ee5b9b9e10292eb721c54a71388dc1afb55ab9196f9bfcb");
insert into Admins (username, password) values ("admin3","a87230fc1013853652e01d84e4e3751b33d0989fbc5a9d08db2e03b1fee4917b4f239f6ab0d4f1e8fd373fb29bc7a48920a39a00fce7dbb2e25096b5d82d6101074fb102bedeaf49bb5183de31ce31d31fb1fcea81f1adc5cc0ee4298a043437");
insert into Admins (username, password) values ("admin4","317b0d9b4acf290b5b77076121a8444f11acacc0eda71160563e84de28bccc1b48d0b2207f06f6d45bde9acffe3ee96031d1ec20925a5e3a075116c2e85f96edecca86d99c33709ef7e64fa0c44f2db617315eb03e5c20d796e243fa34090b6f");
insert into Admins (username, password) values ("admin5","d804e0a1d1c4c20ac396570bd7d2cecfa5a18eae733a4e4b32d45446f174f628040190da9736cd74821db752efebbd1a9dd76a19e52d1858de8163ecddaaa389a1d7750f24d75f5000a8df3667076ee29b5af03a37721a6e5d8693185bd3d02c");
insert into Admins (username, password) values ("admin6","657becc73be7a88ce841b700b86a50011ec491ed2d4a5d2bb91ee3051460485b82a3c199c50ae479d7e09d37c871115ffa4c872adafb7bc0a25c6f16cb12507d1680b67238bc19703589dea54f7e7122e5ff5834e9989d00f906101046ff6afb");
insert into Admins (username, password) values ("admin7","fbb36bde41665f4439676ec864d4fdc30b09ca84eb794365647bac12795496a4303591743dc3767545e81480677a65feefcf996b435438effc85a2dd36c50eb4464a12cc3a5ab70e687acd0e008739b1c2ed0b69d107be1ba66bc1ba84ce50ff");
insert into Admins (username, password) values ("admin8","8f38661ed8f03217f6c234ea9d4195bcea5a1c8d7ac2a326ec8571b855362de31eef14a862add6bdf479244c41cc6b729244a70653a20e53543eabc4dcdd6455ae52ab7bca2696ca503a42540c12e4b4e075b6ea1a14b110f93e2d18e6936d18");
insert into Admins (username, password) values ("admin9","98d98e09f3945cf3f57f5365ae2dc5ca1dc047dd61ca5a5161805b5e843a580e7566b9adbe36dd9bd021cc95d6bef7818ceb9cfc2ecfbc0f18eb6909d29983be9573e79bca4ccb85879ac84dfba94f67221d287512222ec202db5e94eb88366d");
insert into Admins (username, password) values ("admin10","3f2c00f4356f6244eb37c6b3ad68c635d3efce2ab9aacbdfe5b8ced4ca40e50d55c9a89317b6375403dab9ccaa3f9fa0596e03ab98fc36bd1975b034d40a41836bc530673c5b892a80da1d7d27ccbbd5e5239f4d16b20e2e6ce1d8cabdc6723b");
drop table if exists Cars;
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
);
insert into Cars (name, colour, description, capacity , registration_plate , fuel_type, transmission, type, status, price, longitude, latitude, image) values ("Alfa Romeo Spider", "Mettalic Red", "bla bla bla bla bla", 2, "aaa111", 0, 1, "Coupe", 0, 35, 144.664, -37.6152, "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRxKXtjfw7J1wKPnUkDd8WsnPSjpiS6nvEV1w&usqp=CAU");
insert into Cars (name, colour, description, capacity , registration_plate , fuel_type, transmission, type, status, price, longitude, latitude, image) values ("Roll Royce Phantom", "Black", "bla bla bla bla bla", 5, "uhfi34", 4, 0, "Sedan", 1, 37, 144.364, -37.8152, "https://d3e706rdykep76.cloudfront.net/wp-content/uploads/sites/2/2016/10/RollsRoycePhantomBlackFront-1.jpg");
insert into Cars (name, colour, description, capacity , registration_plate , fuel_type, transmission, type, status, price, longitude, latitude, image) values ("Bentley Bentayga", "Blue", "bla bla bla bla bla", 5, "489yt4", 3, 1, "Sedan", 0, 41, 144.964, -37.8152, "https://cdn.motor1.com/images/mgl/6W7vX/s1/bentley-bentayga-design-series.jpg");
insert into Cars (name, colour, description, capacity , registration_plate , fuel_type, transmission, type, status, price, longitude, latitude, image) values ("Lamborghini Vintage", "Yellow", "bla bla bla bla bla", 2, "4h3u723", 2, 0, "Coupe", 1, 32, 144.764, -37.8152, "https://www.wired.com/images_blogs/autopia/2010/09/lamborghini-miura-sv-01.jpg");
insert into Cars (name, colour, description, capacity , registration_plate , fuel_type, transmission, type, status, price, longitude, latitude, image) values ("Pajero Sport", "White", "bla bla bla bla bla", 6, "hg34uht", 3, 1, "SUV", 1, 42, 144.964, -37.8102, "https://motoring.pxcrush.net/motoring/general/editorial/mitsubishi-pajero-sport-154.jpg?width=1024");
insert into Cars (name, colour, description, capacity , registration_plate , fuel_type, transmission, type, status, price, longitude, latitude, image) values ("Ferrari la Ferrari", "Red", "bla bla bla bla bla", 2, "fhewu", 4, 1, "Coupe", 1, 39, 144.764, -37.8102, "https://api.ferrarinetwork.ferrari.com/v2/network-content/medias/resize/5ddb97392cdb32285a799dfa-laferrari-2013-share?apikey=9QscUiwr5n0NhOuQb463QEKghPrVlpaF&width=1080");
insert into Cars (name, colour, description, capacity , registration_plate , fuel_type, transmission, type, status, price, longitude, latitude, image) values ("Porsche 911", "Black", "bla bla bla bla bla", 2, "4ttofw", 2, 1, "Coupe", 0, 37, 144.954, -37.8102, "https://newsroom.porsche.com/.imaging/mte/porsche-templating-theme/image_1080x624/dam/porsche_newsroom/Produkte/911/911-Carrera-Black-Edition/P15_0437_a4_rgb/jcr:content/Black-Edition-3300x1860-MS-mittig.jpg");
insert into Cars (name, colour, description, capacity , registration_plate , fuel_type, transmission, type, status, price, longitude, latitude, image) values ("MINI Cooper", "Brown", "bla bla bla bla bla", 5, "gj34uh4", 1, 0, "Hatchback", 0, 34, 144.634, -37.8150, "https://i.pinimg.com/originals/f7/7f/80/f77f806b88112c65088ad3ecf17a231a.jpg");
insert into Cars (name, colour, description, capacity , registration_plate , fuel_type, transmission, type, status, price, longitude, latitude, image) values ("Honda Civic", "Silver", "bla bla bla bla bla", 5, "4gh33es", 2, 1, "Sedan", 0, 40, 144.604, -37.8040, "https://media.caradvice.com.au/image/private/c_fill,q_auto,f_auto,w_400,ar_16:9/trnfkpxmizhxcaalmsj9.jpg");
insert into Cars (name, colour, description, capacity , registration_plate , fuel_type, transmission, type, status, price, longitude, latitude, image) values ("BMW M5", "Black", "bla bla bla bla bla", 5, "u49394", 2, 1, "Sallon", 1, 40, 144.624, -37.8120, "https://i.redd.it/2aciz8dn5ld31.jpg");
drop table if exists Licenses;
create table if not exists Licenses (
    license_id int not null auto_increment,
    cust_id int not null,
    license_num text not null,
    country text not null,
    state text not null,
    issue_date date not null, 
    expiry_date date not null, 
    constraint PK_License primary key (license_id)
);
insert into Licenses (cust_id, license_num , country, state, issue_date, expiry_date) values(1, "abcd1234","Australia","VIC","2015-12-01", "2020-12-01");
insert into Licenses (cust_id, license_num , country, state, issue_date, expiry_date) values(2, "aaaaaaaa","Australia","VIC","2015-12-02", "2020-12-02");
insert into Licenses (cust_id, license_num , country, state, issue_date, expiry_date) values(3, "11111111","Australia","VIC","2015-12-03", "2020-12-03");
insert into Licenses (cust_id, license_num , country, state, issue_date, expiry_date) values(4, "bbbbbbbb","Australia","VIC","2015-12-04", "2020-12-04");
insert into Licenses (cust_id, license_num , country, state, issue_date, expiry_date) values(5, "abcd1234","Australia","VIC","2015-12-01", "2020-12-05");
insert into Licenses (cust_id, license_num , country, state, issue_date, expiry_date) values(6, "cccccccc","Australia","VIC","2015-12-02", "2020-12-06");
insert into Licenses (cust_id, license_num , country, state, issue_date, expiry_date) values(7, "22222222","Australia","VIC","2015-12-03", "2020-12-07");
insert into Licenses (cust_id, license_num , country, state, issue_date, expiry_date) values(8, "33333333","Australia","VIC","2015-12-04", "2020-12-08");
insert into Licenses (cust_id, license_num , country, state, issue_date, expiry_date) values(9, "dddddddd","Australia","VIC","2015-12-03", "2020-12-09");
insert into Licenses (cust_id, license_num , country, state, issue_date, expiry_date) values(10, "xxxx1111","Australia","VIC","2015-12-04", "2020-12-10");
drop table if exists Addresses;
create table if not exists Addresses (
    address_id int not null auto_increment,
    cust_id int not null,
    unit_no text not null,
    street text not null,
    suburb text not null, 
    state text not null,
    postcode int not null,
    latitude float not null,
    longitude float not null,
    constraint PK_Addresses primary key (address_id)
);
insert into Addresses (cust_id, unit_no, street, suburb, state, postcode, latitude, longitude) values (1, 101,"1st Avenue","Melbourne CBD","VIC", "3000",-37.8152,144.964);
insert into Addresses (cust_id, unit_no, street, suburb, state, postcode, latitude, longitude) values (2, 102,"1st Avenue","Melbourne CBD","VIC", "3000",-37.8152,144.964);
insert into Addresses (cust_id, unit_no, street, suburb, state, postcode, latitude, longitude) values (3, 103,"1st Avenue","Melbourne CBD","VIC", "3000",-37.8152,144.964);
insert into Addresses (cust_id, unit_no, street, suburb, state, postcode, latitude, longitude) values (4, 104,"1st Avenue","Melbourne CBD","VIC", "3000",-37.8152,144.964);
insert into Addresses (cust_id, unit_no, street, suburb, state, postcode, latitude, longitude) values (5, 201,"Russel Lane","Docklands","VIC", "3008",37.8171,144.942);
insert into Addresses (cust_id, unit_no, street, suburb, state, postcode, latitude, longitude) values (6, 202,"Queens Street","Hawthorn","VIC", "3122",-37.8222,145.033);
insert into Addresses (cust_id, unit_no, street, suburb, state, postcode, latitude, longitude) values (7, 203,"King Road","Kew","VIC", "3101",-37.8035,145.033);
insert into Addresses (cust_id, unit_no, street, suburb, state, postcode, latitude, longitude) values (8, 204,"Rose Avenue","Camberwell","VIC", "3124",-37.8334,145.066);
insert into Addresses (cust_id, unit_no, street, suburb, state, postcode, latitude, longitude) values (9, 301,"Lily Road","South Yarra","VIC", "3141",-37.8386,144.991);
insert into Addresses (cust_id, unit_no, street, suburb, state, postcode, latitude, longitude) values (10, 302,"3rd Avenue","Melbourne CBD","VIC", "3000",-37.8152,144.964);
drop table if exists Bookings;
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
);
insert into Bookings (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status) values (1, 1, "2020-12-29","15:55", "2020-12-30", "15:55", "24:00:00", 840, 1);
insert into Bookings (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status) values (1, 8, "2020-01-09","15:55", "2020-01-10", "15:55", "24:00:00", 720, 2);
insert into Bookings (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status) values (1, 9, "2020-08-09","15:55", "2020-08-10", "15:55", "24:00:00", 984, 0);
insert into Bookings (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status) values (2, 7, "2020-09-09","15:55", "2020-09-10", "15:55", "24:00:00", 816, 2);
insert into Bookings (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status) values (2, 9, "2020-12-29","15:25", "2020-12-30", "15:55", "24:30:00", 857.5, 2);
insert into Bookings (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status) values (2, 1, "2020-12-29","15:25", "2020-12-30", "15:55", "24:30:00", 857.5, 1);
insert into Bookings (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status) values (3, 2, "2020-12-29","15:15", "2020-12-29", "16:15", "01:00:00", 32, 0);
insert into Bookings (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status) values (3, 3, "2020-12-29","15:15", "2020-12-29", "16:15", "01:00:00", 32, 1);
insert into Bookings (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status) values (4, 4, "2020-12-28","15:05", "2020-12-28", "18:55", "03:50:00", 141.83, 2);
insert into Bookings (cust_id, car_id, start_date, start_time, end_date, end_time, total_time, total_cost, status) values (4, 5, "2020-12-28","15:05", "2020-12-28", "18:55", "03:50:00", 141.83, 0);
drop table if exists Customers;
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
);
insert into Customers (fname, lname, dob, email, password, phone, plan, premium_expiry) values ("Vincent","Pranata", "1999-12-28","test@1234.com", "6aeb9148d56048bcf9d5c576a7b876bdf1d1029ae6ce0087e0ff48b4e0cd8549e5452a38620eaaa29bde1c9625b5364199a7531c523922ea3b3238aae691d65f58089e1567f162573392d1565a5601f3235c8bde61feb7b65a41b0442de11c90", 123456789, 0, NULL);
insert into Customers (fname, lname, dob, email, password, phone, plan, premium_expiry) values ("Jerald","Tienzo","1999-01-02","test@1111.com", "e1fa918d65f8b84366d1c4766ee02f22f6867802b462d4dd52f664a0cf54f3a0761422b25fd221c11c8eb351ea3e3183f9f1786b8e419c7f26169494e2574b762ffeb9052dfc91522347dbeb304c9dea871424f8e8456b67ffdb0f974de47235", 123456789, 1, "2020-10-20");
insert into Customers (fname, lname, dob, email, password, phone, plan, premium_expiry) values ("Youxin","Zheng","1999-01-01","test@2222.com", "8194f69c8a876dcfe2920154b8844bf2dfa17a90f09584b777a5a2c07ccb9c28818e9d376ad4ac1f8afe79bab6ee407f6cdd1cdf7935237c37dfeba7f66289df06c9c607095b0edbb5249ae442f98a1de59d719d93c1224741635441541a7c85", 123456789, 0, "2020-10-12");
insert into Customers (fname, lname, dob, email, password, phone, plan, premium_expiry) values ("Yanfang","He","1999-01-03","test@3333.com", "6db301585bbdfe98234e14d700fb75ab03aab2cabe2e3fc0e73f57b4044471c69efbc51e866110f82ab7f184ca8f5865b89a897b5dc20f38d041df774c7a59698b7cc58a2cd8ac3cb148269425ec051697c589bb677cc8ce69fa63102645081a", 123456789, 1, "2020-11-10");
insert into Customers (fname, lname, dob, email, password, phone, plan, premium_expiry) values ("Test","123","1991-11-28","test@4444.com", "ed701a7f1ccd9fd97370920cf95c632b2cf88015f01f04954f6b2ec3810e593106beb895c2e3f5981ee08a30472778986e8e7171ee70ce7051f0f553dfd1a1f219acd5bab14e64ba818d7589666c1e64149d762f0ffc498e55c160a490022502", 123456789, 0, NULL);
insert into Customers (fname, lname, dob, email, password, phone, plan, premium_expiry) values ("Abc","123","1994-03-01","test@5555.com", "23273bc09cff10f0290a0fae79930e1aef3ee4cb69c417baaece51852931f398fac431a499e9f90a7df382d7fe345efa82519e6e8cbd63d212993212ca591a0fe258594458ebf470f9fa766679af56bd11ff528109344f15fc97dc68d1af2b79", 123456789, 1, "2020-11-20");
insert into Customers (fname, lname, dob, email, password, phone, plan, premium_expiry) values ("212","Def","1995-02-02","test@6666.com", "9d0a685900f85789f878919c20aa805583f12c0363605335c164a3012df2eff2678c303c055ed89c6d07a091df20da7b814fc07fd9907db9108fb9fe4611941a52e104e5c994808673ab3faef2b5bc3c13a8c81b079635cf0b9a843661c71741", 123456789, 0, "2020-12-12");
insert into Customers (fname, lname, dob, email, password, phone, plan, premium_expiry) values ("Abc","xxx","1997-11-03","test@7777.com", "0f9ee0ea469c275cb5fa43a74d1b067291779a83a9a281e29d4c7cd0e32268ff238128ea7b9b9723a26906a200b7bcb58d7ec263d11110f3049622237e7b230554c774559e20c7abdc0c4935628186e98ee995022ce29b0d94324ebe7a0742da", 123456789, 0, NULL);
insert into Customers (fname, lname, dob, email, password, phone, plan, premium_expiry) values ("Swefwe","saae","1998-11-28","test@8888.com", "108e58f92bf5c2566c6a6b0fcb34724fe60ea45c87e15788607664bc594b931dddbe5b025713e4b985b539550df67c0b0ee534eb1a5c25e345956646058480238bdd320b9bc5f4a5e72d5b994af30e98b09efaa791358e67afb9d6f9cc7b683c", 123456789, 0, NULL);
insert into Customers (fname, lname, dob, email, password, phone, plan, premium_expiry) values ("Jerald","Tienzo","2000-11-21","test@9999.com", "1418000853d1d77daad7fe838f19a3727d0406e66b57287b29af5557691b184e675d8552e1fa0ea4d7d20221265502b0eee5164041cb54aefd6443fe2385288e7e69c410294f4672f9a9f85d44414ef711bc9dc11df4f0b3062cca79dc04cf04", 123456789, 0, NULL);

from faker.proxy import Faker

global email, username, password, first_name, last_name, address, city, state, zipcode, mobile_number, \
    card_number, cvc, card_month, card_year

def initialize_registration_data():
    global email, username, password, first_name, last_name, address, city, state, zipcode, mobile_number, \
        card_number, cvc, card_month, card_year
    f = Faker()
    email = f.email()
    username = f.user_name()
    password = f.password()
    first_name = f.first_name()
    last_name = f.last_name()
    address = f.address()
    city = f.city()
    state = f.state()
    zipcode = f.zipcode()
    mobile_number = f.phone_number()
    card_number = f.credit_card_number()
    cvc = f.credit_card_security_code()
    card_month = f.month()
    card_year = f.year()

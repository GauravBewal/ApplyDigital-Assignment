from playwright.sync_api import expect


class PlaceOrder:

    def __init__(self, page):
        self.page = page
        self.products_tab = "//a[contains(text(),'Products')]"
        self.third_product = "//div[@id='cartModal']//following-sibling::div[3]//a[contains(text(),'View Product')]"
        self.quantity = "//input[@id='quantity']"
        self.add_to_cart = "//button[contains(@class,'cart')]"
        self.view_cart = "//u[contains(text(),'View Cart')]"
        self.proceed_to_checkout = "//a[contains(text(),'Proceed To Checkout')]"
        self.register_login = "//u[contains(text(),'Register')]"
        self.register_username = "//input[@data-qa='signup-name']"
        self.register_email = "//input[@data-qa='signup-email']"
        self.registration_page_header = "//b[contains(text(),'Enter Account Information')]"
        self.register_password = "//input[@data-qa='password']"
        self.address = "//input[@data-qa='address']"
        self.state = "//input[@data-qa='state']"
        self.first_name = "//input[@data-qa='first_name']"
        self.last_name = "//input[@data-qa='last_name']"
        self.city = "//input[@data-qa='city']"
        self.zipcode = "//input[@data-qa='zipcode']"
        self.mobile_number = "//input[@data-qa='mobile_number']"
        self.create_account = "//button[@data-qa='create-account']"
        self.account_created = "//b[contains(text(),'Account Created')]"
        self.continue_button = "//a[@data-qa='continue-button']"
        self.view_cart_tab = "//a[contains(text(),'Cart') and contains(@href,'cart')]"
        self.place_order = "//a[contains(text(),'Place Order')]"
        self.name_on_card = "//input[@data-qa='name-on-card']"
        self.card_number = "//input[@data-qa='card-number']"
        self.cvc = "//input[@data-qa='cvc']"
        self.expiry_month = "//input[@data-qa='expiry-month']"
        self.expiry_year = "//input[@data-qa='expiry-year']"
        self.submit = "//button[@data-qa='pay-button']"
        self.logout = "//a[contains(text(),'Logout')]"
        self.order_placed = "//b[contains(text(),'Order Placed')]"
        self.signup_button = "//button[@data-qa='signup-button']"


    def click_products_tab(self):
        return self.page.locator(self.products_tab).click()

    def click_view_details_of_third_product(self):
        return self.page.locator(self.third_product).click()

    def enter_quantity(self, quantity):
        return self.page.locator(self.quantity).fill(quantity)

    def click_add_to_cart(self):
        return self.page.locator(self.add_to_cart).click()

    def click_view_cart(self):
        return self.page.locator(self.view_cart).click()

    def click_proceed_to_checkout(self):
        return self.page.locator(self.proceed_to_checkout).click()

    def click_register_login(self):
        return self.page.locator(self.register_login).click()

    def enter_signup_details(self, reg_username, reg_email):
        self.page.locator(self.register_username).fill(reg_username)
        return self.page.locator(self.register_email).fill(reg_email)

    def enter_account_info(self, reg_password, first_name, last_name, address, city, state, zipcode, mobile_number):
        self.page.locator(self.register_password).fill(reg_password)
        self.page.locator(self.first_name).fill(first_name)
        self.page.locator(self.last_name).fill(last_name)
        self.page.locator(self.address).fill(address)
        self.page.locator(self.state).fill(state)
        self.page.locator(self.city).fill(city)
        self.page.locator(self.zipcode).fill(zipcode)
        return self.page.locator(self.mobile_number).fill(mobile_number)

    def click_create_account(self):
        return self.page.locator(self.create_account).click()

    def click_continue_button(self):
        return self.page.locator(self.continue_button).click()

    def click_view_cart_tab(self):
        return self.page.locator(self.view_cart_tab).click()

    def click_place_order(self):
        return self.page.locator(self.place_order).click()

    def click_submit(self):
        return self.page.locator(self.submit).click()

    def enter_card_details(self, name_on_card, card_number, cvc, expiry_month, expiry_year):
        self.page.locator(self.name_on_card).fill(name_on_card)
        self.page.locator(self.card_number).fill(card_number)
        self.page.locator(self.cvc).fill(cvc)
        self.page.locator(self.expiry_month).fill(expiry_month)
        return self.page.locator(self.expiry_year).fill(expiry_year)

    def click_logout(self):
        return self.page.locator(self.logout).click()

    def click_signup_button(self):
        return self.page.locator(self.signup_button).click()
    
    def verify_account_created_msg(self):
        expect(self.page.locator(self.account_created)).to_be_visible(timeout=30000)

    def verify_order_placed_msg(self):
        expect(self.page.locator(self.order_placed)).to_be_visible(timeout=30000)

    def verify_signup_button(self):
        expect(self.page.locator(self.signup_button)).to_be_visible(timeout=30000)

    def verify_guid_overview(self):
        expect(self.page.locator(self.guid_header)).to_be_visible(timeout=30000)
        expect(self.page.locator(self.guid_value)).to_contain_text("40DD879C-EE2F-11DB-8314-0800200C9A26")

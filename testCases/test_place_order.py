from pytest_playwright.pytest_playwright import page
import pytest
from pageObject.placeOrder import PlaceOrder
from utilities.base import Base
import testData.registration_data as reg_data

from utilities.common_functions import get_random_number


@pytest.mark.usefixtures("setup_teardown")
class TestPlaceOrder(Base):

    @pytest.mark.smoke
    def test_place_order(self, page):
        # Initialization of the class objects

        log = Base.getlogger(self)
        reg_data.initialize_registration_data()
        po = PlaceOrder(page)
        po.click_products_tab()
        log.info("Homepage is visible, clicked on the Product Tab")
        po.click_view_details_of_third_product()


        # Adding Product into the cart

        log.info("Clicked on the 3rd Product, View Details")
        po.enter_quantity(quantity=get_random_number())
        log.info("Quantity entered - "+get_random_number())
        po.click_add_to_cart()
        log.info("Clicked on Add to cart button")
        po.click_view_cart()
        log.info("Clicked on View Cart Link")
        po.click_proceed_to_checkout()
        log.info("Clicked on Proceed to checkout button")

        # Signup a new user

        po.click_register_login()
        log.info("Clicked on the Register/Login Link")
        po.enter_signup_details(reg_email=reg_data.email, reg_username=reg_data.username)
        po.click_signup_button()
        log.info("Signup details are entered, clicked on the Signup button")
        po.enter_account_info(reg_password=reg_data.password, first_name=reg_data.first_name, last_name=reg_data.last_name,
                              address=reg_data.address, city=reg_data.city, state=reg_data.state,
                              zipcode=reg_data.zipcode, mobile_number=reg_data.mobile_number)
        po.click_create_account()
        po.verify_account_created_msg()
        log.info(f"A New Account is Created Successfully, UserName - {reg_data.username} Email - {reg_data.email}")
        po.click_continue_button()
        log.info("Clicked on the Continue Button")
        po.click_view_cart_tab()
        po.click_proceed_to_checkout()
        log.info("Clicked on the View Cart Tab and then Proceed to Checkout")

        # Entering Payment Details

        po.click_place_order()
        po.enter_card_details(name_on_card=reg_data.username, card_number=reg_data.card_number,
                              cvc=reg_data.cvc, expiry_month=reg_data.card_month, expiry_year=reg_data.card_year)
        po.click_submit()
        log.info("Entered payment details")
        po.verify_order_placed_msg()
        log.info("Order Placed Successfully !")

        # Logout User

        po.click_logout()
        po.verify_signup_button()
        log.info("Clicked on the Logout and Signup Button is visible again.")



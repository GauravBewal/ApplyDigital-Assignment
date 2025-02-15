from playwright.sync_api import expect

from pageObject.basePage import BasePage


class LoginPage:

    def __init__(self, page):
        # super().__init__(page)
        self.page = page
        self.username_locator = "//input[@name='username']"
        self.password_locator = "//input[@name='password']"
        self.submit_locator = "//button[text()='Sign In']"
        self.home_page_header = "//h1[text()='Live Client Query Feed']"

    def enter_username(self, username):
        self.page.locator(self.username_locator).fill(username)

    def enter_password(self, password):
        self.page.locator(self.password_locator).fill(password)

    def click_on_submit(self):
        self.page.locator(self.submit_locator).click()

    def get_homepage_header(self):
        return (self.page.locator(self.home_page_header)).inner_text()

    def verify_homepage_header(self):
        expect(self.page.locator(self.home_page_header)).to_be_visible(timeout=30000)

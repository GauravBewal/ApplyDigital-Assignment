import pytest
from playwright.sync_api import Page, expect, Playwright
from pytest_playwright.pytest_playwright import context, browser
from configurations.readConfigurations import ReadConfig
import allure
import os
import tkinter as tk


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default=ReadConfig.getURL())
    parser.addoption("--username", action="store", default=ReadConfig.getUsername())
    parser.addoption("--password", action="store", default=ReadConfig.getPassword())
    parser.addoption("--maximize", action="store_true", help="Maximize browser window")

@pytest.fixture(scope="session", autouse=True)
def browser_context_args(request):
    if request.config.getoption("--maximize"):
        return {"viewport": None}
    return {}

def get_url(request):
    url = request.config.getoption("url")
    return url

def get_username(request):
    username = request.config.getoption("username")
    return username

def get_password(request):
    password = request.config.getoption("password")
    return password

@pytest.fixture(scope="function")
def setup_teardown(page: Page, request):
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    page.set_viewport_size({'width':width, 'height':height})
    ReadConfig.setUrl(get_url(request))
    ReadConfig.setUsername(get_username(request))
    ReadConfig.setPassword(get_password(request))
    page.goto(ReadConfig.getURL())
    # page.wait_for_timeout(2000)
    # login(page, ReadConfig.getUsername(), ReadConfig.getPassword())
    # page.set_default_timeout(30000)
    # browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
    # context = browser.new_context()
    # page = context.new_page()
    # context.set_default_navigation_timeout(30000)
    # context.set_default_timeout(30000)
    # request.cls.driver = page
    yield page
    # context.close()
    # browser.close()
    page.close()

def login(page, username, password):
    username_locator = "//input[@name='username']"
    password_locator = "//input[@name='password']"
    submit_locator = "//button[text()='Sign In']"
    home_page_header = "//h1[text()='Live Client Query Feed']"
    page.wait_for_selector(selector=username_locator, timeout=10000)
    page.locator(username_locator).fill(username)
    page.locator(password_locator).fill(password)
    page.locator(submit_locator).click()
    expect(page.locator(home_page_header)).to_be_visible(timeout=10000)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to take a screenshot when a test fails and attach it to Allure reports.
    Fixes the 'context' fixture issue by using 'page.context'.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")  # Retrieve the Playwright 'page' fixture
        if page:
            context = page.context  # Get browser context dynamically

            if context.pages:  # Ensure at least one tab exists
                try:
                    active_page = context.pages[-1]  # Get the most recent tab
                    screenshot_path = f"screenshots/{item.name}.png"
                    os.makedirs("screenshots", exist_ok=True)

                    # Check if the page is closed before taking a screenshot
                    if active_page.is_closed():
                        active_page = context.pages[0]  # Fall back to the main tab

                    active_page.screenshot(path=screenshot_path)

                    allure.attach.file(
                        screenshot_path,
                        name="Failure Screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
                except Exception as e:
                    print(f"Error taking screenshot: {e}")  # Log error gracefully

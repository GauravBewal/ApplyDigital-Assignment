import pytest
from playwright.sync_api import Page
from configurations.readConfigurations import ReadConfig
import allure
import os
import tkinter as tk


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default=ReadConfig.getURL())

def get_url(request):
    url = request.config.getoption("url")
    return url


@pytest.fixture(scope="function")
def setup_teardown(page: Page, request):
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    page.set_viewport_size({'width':width, 'height':height})
    page.goto(get_url(request))

    yield page

    page.close()


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

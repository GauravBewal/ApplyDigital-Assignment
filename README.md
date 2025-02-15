# Directory Structure
configuration - Defines a place to put all the configuration related stuff, use config.ini to edit the run configuration

testCases - Place to put all test scripts\conftest

testData - All data will be placed related to testCases will be placed here

reports - All the output reports xml/html and screenshots will come in this directory

testdata - Any testdata related to testing will be put here. eg files, csv, png, json etc

utilities - Base and all common actions related classes files are placed here

pageObjects - All module related pages and elements are placed here

```pip install -r requirements.txt && playwright install```

# Command to run the test case (CLI Command)

```pytest test.py```

```pytest test.py -k <test case name>``` To run a specific test

Options that we can give with CLI Command are - 
```--headed``` 
```--tracing on``` 
```--browser firefox```


# Options that can be use with the trace command

```on```: Record trace for each test

```off```: Do not record trace. (default)

```retain-on-failure```: Record trace for each test, but remove all traces from successful test runs.

# Command to see the traces
```playwright show-trace trace.zip```

# Debugging Test
```PWDEBUG=1 pytest -s```

```PWDEBUG=1 pytest -s test_example.py``` To debug one test file, run the command followed by the name of the test file that you want to debug.

```PWDEBUG=1 pytest -s -k test_get_started_link``` To debug a specific test, add -k followed by the name of the test that you want to debug.

# Parallelism: Running Multiple Tests at Once
```pip install pytest-xdist``` (install dependency)
pytest --numprocesses auto

# Configure base-url
Start Pytest with the base-url argument. The pytest-base-url plugin is used for that which allows you to set the base url from the config, CLI arg or as a fixture.

pytest --base-url http://localhost:8080

# PyTest Fixtures

pytest -s -v -m sanity

# PyTest CLI Commands

To only re-run the failures.
```pytest --lf```

To run the failures first and then the rest of the tests.
```pytest --ff```

Run a single test, using keyword
```pytest -k "login"```

# Screenshots Capturing
If we manually wants to take and attach the screenshot inside a test case.

``` allure.attach(page.screenshot(), name="Homepage Screenshot", attachment_type=allure.attachment_type.PNG)```

# All CLI Arguments 
Note that CLI arguments are only applied to the default browser, context and page fixtures. 
If you create a browser, a context or a page with the API call like browser.new_context(), 
the CLI arguments are not applied.

--headed: Run tests in headed mode (default: headless).
--browser: Run tests in a different browser chromium, firefox, or webkit. It can be specified multiple times (default: chromium).
--browser-channel Browser channel to be used.
--slowmo Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on (default: 0).
--device Device to be emulated.
--output Directory for artifacts produced by tests (default: test-results).
--tracing Whether to record a trace for each test. on, off, or retain-on-failure (default: off).
--video Whether to record video for each test. on, off, or retain-on-failure (default: off).
--screenshot Whether to automatically capture a screenshot after each test. on, off, or only-on-failure (default: off).
--full-page-screenshot Whether to take a full page screenshot on failure. By default, only the viewport is captured. Requires --screenshot to be enabled (default: off).```
# Directory Structure
configuration - Defines a place to put all the configuration related stuff, use config.ini to edit the run configuration

testCases - Place to put all test scripts\conftest

testData - All data will be placed related to testCases will be placed here

reports - All the output allure reports will come in this directory

screenshots - All the failed test cases captured screenshots will come here

logs - All the logs of the test execution will come here

testdata - Any testdata related to testing will be put here. eg files, csv, png, json etc

utilities - Base and all common actions related classes / files are placed here

pageObjects - All module related pages and elements are placed here

CICD - All the pipeline setup related code will come here.


# Pre-requisite -
1. Latest version of Python is installed
2. You are on project root directory

# To run Test Cases - 

Run this command to install all the required libraries- 

```pip install -r requirements.txt && playwright install```

Command to run the test case through (CLI Command)

```pytest <test case file name>.py```

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

# To Open Allure Report -

Run this command - 

```allure serve -h localhost reports```

# Logs
Logs are collected under "logs" folder

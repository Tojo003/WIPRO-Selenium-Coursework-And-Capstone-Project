# Capstone Project 3: Python API Automation Framework with Requests + Behave BDD

## Objective

Build a complete **API Automation Framework** using:

- Python Requests Library
- REST API Testing
- Behave BDD Framework
- Allure Reporting
- Reusable Framework Design

## Project Scenario

Automate the **User Management API** of a sample REST service.

### Suggested APIs

1. JSONPlaceholder  
   https://jsonplaceholder.typicode.com/

2. Automation Exercise API List  
   https://automationexercise.com/api_list

## Project File Structure

```text
Capstone Project/
│
├── api_client.py              <-- Handles all HTTP methods
├── features/
│   ├── environment.py         <-- Manages hooks & Allure environment metadata
│   ├── api_tests.feature      <-- Feature file covering GET, POST, PUT, PATCH, DELETE
│   └── steps/
│       └── api_steps.py       <-- Reusable BDD step definitions
```

## Code Execution Guide
# API Automation Project – Execution Guide

## Prerequisites

Install the following software:

- Python 3.10 or later
- Git
- Java 8 or later
- Allure Commandline

Verify that Python, Java, and Allure are available in PowerShell:

```powershell
python --version
java -version
allure --version
```

## 1. Clone the Repository

```powershell
git clone https://github.com/Tojo003/WIPRO-Selenium-Coursework-And-Capstone-Project.git
cd .\WIPRO-Selenium-Coursework-And-Capstone-Project\
```

## 2. Navigate to the Capstone Project

The project directory contains a space in its name, so use quotes:

```powershell
cd ".\Capestone Project\"
```

Confirm that the expected files are present:

```powershell
Get-ChildItem
Get-ChildItem .\features\
Get-ChildItem .\features\steps\
```

Expected files include:

```text
api_client.py
requirements.txt
PROJECT_REPORT.md
features\
├── environment.py
├── test_api.feature
└── steps\
    └── api_test_steps.py
```

## 3. Create a Python Virtual Environment

```powershell
python -m venv .venv
```

## 4. Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, temporarily allow scripts for the current PowerShell session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the PowerShell prompt should show:

```text
(.venv)
```

## 5. Upgrade pip

```powershell
python -m pip install --upgrade pip
```

## 6. Install Project Dependencies

```powershell
python -m pip install -r .\requirements.txt
```

Verify the installed packages:

```powershell
python -m pip list
```

## 7. Run the Behave API Tests

Run all feature tests:

```powershell
python -m behave
```

The tests use the following Automation Exercise API endpoints:

- `https://automationexercise.com/api/productsList`
- `https://automationexercise.com/api/searchProduct`
- `https://automationexercise.com/api/updateAccount`
- `https://automationexercise.com/api/deleteAccount`

An active internet connection is required.

## 8. Run Tests with Allure Results

Remove old Allure results before a fresh execution:

```powershell
if (Test-Path .\allure-results) {
    Remove-Item .\allure-results -Recurse -Force
}
```

Execute the tests and generate Allure result files:

```powershell
python -m behave `
    -f allure_behave.formatter:AllureFormatter `
    -o .\allure-results
```

The `environment.py` file automatically creates the following metadata file:

```text
allure-results\environment.properties
```

## 9. View the Allure Report

Start a temporary local Allure report server:

```powershell
allure serve .\allure-results
```

Allure will open the report in a browser.

To generate a static report instead:

```powershell
allure generate .\allure-results `
    -o .\allure-report `
    --clean
```

Open the generated report:

```powershell
allure open .\allure-report
```

## 10. Run Specific Feature Scenarios

Run only the API feature file:

```powershell
python -m behave .\features\test_api.feature
```

Run a specific scenario by name:

```powershell
python -m behave `
    .\features\test_api.feature `
    --name "GET - Retrieve Products List"
```

Run scenarios matching a tag:

```powershell
python -m behave --tags=@api
```

## 11. Run Tests with Verbose Output

```powershell
python -m behave -v
```

Run with additional logging:

```powershell
python -m behave --no-capture
```

## 12. Deactivate the Virtual Environment

When testing is complete:

```powershell
deactivate
```

## Recommended Complete Execution Sequence

```powershell
cd "C:\path\to\WIPRO-Selenium-Coursework-And-Capstone-Project\Capestone Project"

python -m venv .venv

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip

python -m pip install -r .\requirements.txt

if (Test-Path .\allure-results) {
    Remove-Item .\allure-results -Recurse -Force
}

python -m behave `
    -f allure_behave.formatter:AllureFormatter `
    -o .\allure-results

allure serve .\allure-results
```

## Troubleshooting

### Python is not recognized

Install Python and ensure that the option to add Python to `PATH` is enabled. Then reopen PowerShell.

### Virtual environment activation is blocked

Run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Allure is not recognized

Install Allure Commandline and ensure its `bin` directory is included in the system `PATH`.

Verify the installation:

```powershell
allure --version
```

### Tests cannot connect to the API

Check the following:

- Internet connectivity
- API availability
- Firewall or proxy settings
- Correct endpoint URLs
- Whether the API service is temporarily unavailable

### Import errors occur

Ensure that the command is executed from the project directory:

```powershell
cd ".\Capestone Project\"
```

Also confirm that the virtual environment is active:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Tools, Software, and Concepts Used

This project uses the following tools, software, libraries, and software testing concepts:

### Tools and Software

- **Python 3.10 or later** – Used as the primary programming language.
- **Requests Library** – Used to send HTTP requests to REST API endpoints.
- **Behave BDD Framework** – Used to write and execute behavior-driven test scenarios.
- **Allure Report** – Used to generate detailed and user-friendly test execution reports.
- **Git and GitHub** – Used for source code management and project collaboration.
- **Java** – Required for running the Allure Commandline tool.
- **PowerShell** – Used to create the virtual environment, install dependencies, and execute tests.

### Concepts Used

- REST API testing
- HTTP methods such as `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`
- API endpoints and request URLs
- Request payloads and parameters
- JSON response parsing
- HTTP status code validation
- Response body validation
- Positive and negative test scenarios
- Behavior-Driven Development using Gherkin syntax
- Reusable step definitions
- Test setup and teardown hooks
- Test reporting and environment metadata
- Assertions and test failure analysis
- Python virtual environments and dependency management

## Brief Result, Observation, and Conclusion

### Result

The API automation framework was implemented successfully using Python, Requests, Behave, and Allure. The test suite covers multiple REST API operations, including retrieving products, searching products with missing parameters, updating a non-existent account, and deleting an account.

The tests validate:

- HTTP status codes
- JSON response codes
- Response body messages
- Request payload handling
- Different HTTP request methods
- API behavior for both valid and invalid requests

### Observations

- The Requests library provides a simple and effective way to communicate with REST APIs.
- Behave feature files make the test scenarios easy to read and understand.
- Reusable step definitions reduce duplicate code and make the framework easier to maintain.
- The API consistently returns HTTP status code `200` while providing the actual operation result through the JSON `responseCode` field.
- Negative test cases are useful for verifying how the API handles missing parameters and non-existent user accounts.
- Allure captures request information, response data, execution metadata, environment details, and failure logs.
- The framework requires an active internet connection because the tests use live Automation Exercise API endpoints.

### Conclusion

This project demonstrates the successful implementation of a reusable REST API automation framework using Python Requests, Behave BDD, and Allure reporting.

The framework can validate API functionality, response status codes, JSON response content, and error-handling behavior. Its modular structure separates the API client, feature scenarios, step definitions, and test hooks, making the project easier to understand, maintain, and expand.

Future improvements could include adding authentication testing, request headers, timeout handling, response schema validation, parameterized test data, logging, retry mechanisms, and integration with a continuous integration pipeline.
Then reinstall the dependencies:

```powershell
python -m pip install -r .\requirements.txt
```

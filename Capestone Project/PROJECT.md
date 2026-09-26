# Capstone Project 3: Python API Automation Framework with Requests + Behave BDD

## Objective

Build a complete **API Automation Framework** using:

- Python Requests Library
- REST API Testing
- Authentication
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

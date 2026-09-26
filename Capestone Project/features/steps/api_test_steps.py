import json
import allure
from behave import given, then, when
import api_client


@given('the target endpoint URL is "{url}"')
def step_set_url(context, url):
    context.url = url
    context.payload = {}

@given('request payload parameter "{key}" is set to "{value}"')
def step_set_payload_param(context, key, value):
    if not hasattr(context, "payload") or context.payload is None:
        context.payload = {}
    context.payload[key] = value

@when('I send a "{method}" request')
def step_send_simple_request(context, method):
    _execute_and_attach(context, method.upper(), payload=None)

@when('I send a "{method}" request with payload')
def step_send_payload_request(context, method):
    payload = getattr(context, "payload", None)
    _execute_and_attach(context, method.upper(), payload=payload)
    context.payload = {}

def _execute_and_attach(context, method, payload=None):
    with allure.step(f"Executing HTTP {method} request to {context.url}"):
        if payload:
            allure.attach(
                json.dumps(payload, indent=4),
                name="Request Payload",
                attachment_type=allure.attachment_type.JSON,
            )

        if method == "GET":
            context.api_data = api_client.send_get_request(context.url)
        elif method == "POST":
            context.api_data = api_client.send_post_request(
                context.url, payload
            )
        elif method == "PUT":
            context.api_data = api_client.send_put_request(context.url, payload)
        elif method == "PATCH":
            context.api_data = api_client.send_patch_request(
                context.url, payload
            )
        elif method == "DELETE":
            context.api_data = api_client.send_delete_request(
                context.url, payload
            )
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        allure.attach(
            f"URL: {context.url}\nMethod: {context.api_data['method']}\nStatus Code: {context.api_data['status_code']}",
            name="Execution Metadata",
            attachment_type=allure.attachment_type.TEXT,
        )

        allure.attach(
            context.api_data["formatted_json"],
            name="Response Output",
            attachment_type=allure.attachment_type.JSON,
        )

@then("the HTTP status code should be {status_code:d}")
def step_assert_http_status(context, status_code):
    with allure.step(f"Assert HTTP status code equals {status_code}"):
        actual_code = context.api_data["status_code"]
        assert (
            actual_code == status_code
        ), f"Expected HTTP status {status_code}, got {actual_code}"

@then("the JSON responseCode should be {res_code:d}")
def step_assert_json_response_code(context, res_code):
    with allure.step(f"Assert JSON responseCode equals {res_code}"):
        json_data = context.api_data["json_data"]
        actual_res_code = json_data.get("responseCode")
        assert (
            actual_res_code == res_code
        ), f"Expected JSON responseCode {res_code}, but got {actual_res_code}"

@then('the response body message should be "{expected_message}"')
def step_assert_json_message(context, expected_message):
    with allure.step(f"Assert message equals '{expected_message}'"):
        json_data = context.api_data["json_data"]
        actual_message = json_data.get("message")
        assert (
            actual_message == expected_message
        ), f"Expected message '{expected_message}', got '{actual_message}'"
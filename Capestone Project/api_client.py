import json
import requests


def _process_response(response):
    method = response.request.method
    code = response.status_code

    try:
        json_data = response.json()
        formatted_json = json.dumps(json_data, indent=4)
    except Exception:
        json_data = {}
        formatted_json = response.text

    print(f"Method: {method}")
    print(f"Code: {code}")
    print(f"Response:\n{formatted_json}")

    return {
        "status_code": code,
        "method": method,
        "formatted_json": formatted_json,
        "json_data": json_data,
        "raw_response": response,
    }

def send_get_request(url):
    """Executes HTTP GET request."""
    response = requests.get(url)
    return _process_response(response)

def send_post_request(url, payload=None):
    """Executes HTTP POST request."""
    response = requests.post(url, data=payload)
    return _process_response(response)

def send_put_request(url, payload=None):
    """Executes HTTP PUT request."""
    response = requests.put(url, data=payload)
    return _process_response(response)

def send_delete_request(url, payload=None):
    """Executes HTTP DELETE request."""
    response = requests.delete(url, data=payload)
    return _process_response(response)
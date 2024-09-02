import requests
from requests.exceptions import RequestException
import time

# URL to send requests to
url = 'https://localhost:7010'  # Use http if HTTPS is not configured

# Number of requests to send
num_requests = 100000

# Time to wait between requests (in seconds)
delay = 1

def send_requests(url, num_requests):
    for i in range(num_requests):
        try:
            response = requests.get(url, verify=False)  # Set verify=True in production
            print(f"Request {i + 1}: Status Code {response.status_code}, Response Time: {response.elapsed.total_seconds()}s")
        except RequestException as e:
            print(f"Request {i + 1}: Failed with error {e}")
        time.sleep(delay)  # Delay between requests

if __name__ == "__main__":
    send_requests(url, num_requests)

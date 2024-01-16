import requests

import logging
def make_http_get_request(url):
    try:
        response = requests.get(url)
        logging.info(f"Response code: {response.status_code}")
        return response
    except requests.exceptions.ConnectionError as e:
        logging.error(f"Connection error: {e}")
    except requests.exceptions.Timeout as e:
        logging.error(f"Timeout error: {e}")
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
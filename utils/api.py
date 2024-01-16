import requests
import traceback

import logging


def make_http_get_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        elif response.status_code == 404:
            logging.error(f"The URL '{url}' not found")
            return None
        elif response.status_code == 500:
            logging.error(f"Internal server error at '{url}'")
            return None
        elif response.status_code == 400:
            logging.error(f"Bad request at '{url}'")
            return None
    except requests.exceptions.ConnectionError as e:
        logging.error(f"Connection error: {traceback.print_exc()}")
    except requests.exceptions.Timeout as e:
        logging.error(f"Timeout error: {traceback.print_exc()}")
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error: {traceback.print_exc()}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {traceback.print_exc()}")

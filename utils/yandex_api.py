import requests
import urllib.parse
import logging

YANDEX_API_URL = 'https://cloud-api.yandex.net/v1/disk/'

# Function to get a list of files on Yandex Disk
def get_file_list(public_key):
    headers = {
        'Authorization': f'OAuth {public_key}'
    }
    response = requests.get(YANDEX_API_URL + 'resources/files', headers=headers)
    
    if response.status_code == 200:
        return response.json()['items']
    else:
        logging.error(f"Failed to fetch file list. Status Code: {response.status_code}")
        return None

# Function to get Yandex Disk user information
def get_user_info(public_key):
    headers = {
        'Authorization': f'OAuth {public_key}'
    }
    response = requests.get(YANDEX_API_URL, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Failed to fetch user information. Status Code: {response.status_code}")
        return None

# Function to get the download URL for a specific file
def get_download_url(public_key, file_path):
    headers = {
        'Authorization': f'OAuth {public_key}'
    }

    # Log the original file path
    logging.debug(f"Original file path: {file_path}")

    # Remove 'disk:' prefix if present
    if file_path.startswith('disk:'):
        file_path = file_path.replace('disk:', '')

    # Log the file path after modification
    logging.debug(f"File path after removing 'disk:': {file_path}")

    # URL-encode the file path
    encoded_file_path = urllib.parse.quote(file_path)

    # Log the encoded file path
    logging.debug(f"Encoded file path: {encoded_file_path}")

    # Make the API request to get the download URL
    response = requests.get(
        YANDEX_API_URL + 'resources/download',
        params={'path': encoded_file_path},
        headers=headers
    )

    # Log the response status and content
    logging.debug(f"Download response: {response.status_code} - {response.text}")

    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Failed to get download URL. Status Code: {response.status_code}")
        return None

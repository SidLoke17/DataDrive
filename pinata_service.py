import os
import requests

PINATA_API_KEY = os.getenv('PINATA_API_KEY')
PINATA_API_SECRET = os.getenv('PINATA_API_SECRET')
PINATA_BASE_URL = 'https://api.pinata.cloud'

def pin_file_to_pinata(filepath, filename):
    url = f"{PINATA_BASE_URL}/pinning/pinFileToIPFS"
    headers = {
        'pinata_api_key': PINATA_API_KEY,
        'pinata_secret_api_key': PINATA_API_SECRET
    }
    with open(filepath, 'rb') as file:
        response = requests.post(url, files={'file': (filename, file)}, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to pin file", "details": response.text}

def pin_json_to_pinata(json_data):
    url = f"{PINATA_BASE_URL}/pinning/pinJSONToIPFS"
    headers = {
        'pinata_api_key': PINATA_API_KEY,
        'pinata_secret_api_key': PINATA_API_SECRET,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=json_data, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to pin JSON", "details": response.text}

def list_pinned_files_from_pinata():
    url = f"{PINATA_BASE_URL}/data/pinList"
    headers = {
        'pinata_api_key': PINATA_API_KEY,
        'pinata_secret_api_key': PINATA_API_SECRET
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to list pinned files", "details": response.text}

def unpin_file_from_pinata(ipfs_hash):
    url = f"{PINATA_BASE_URL}/pinning/unpin/{ipfs_hash}"
    headers = {
        'pinata_api_key': PINATA_API_KEY,
        'pinata_secret_api_key': PINATA_API_SECRET
    }
    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        return {"message": "File unpinned successfully"}
    else:
        return {"error": "Failed to unpin file", "details": response.text}

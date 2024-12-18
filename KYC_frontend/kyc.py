import requests
import json
from pathlib import Path
from web3.auto import w3

# Pinata API headers (keep secrets directly in the code for this example)
headers = {
    "Content-Type": "application/json",
    "pinata_api_key": "068352793a74c64dadef",  # Your Pinata API key
    "pinata_secret_api_key": "3b7ce5e9afee74610b2be9035cf8e765fa877924aaf4c5072722c84bc5a546a7",  # Your Pinata Secret API key
}

def initContract():
    """
    Initialize the KYC smart contract using its ABI and address from environment variables.
    """
    try:
        # Load ABI from a JSON file
        with open(Path("KYC.json")) as json_file:
            abi = json.load(json_file)
        
        # Hardcoded contract address (your KYC smart contract address)
        contract_address = "0x8c70021953647d6469d3bc999C76249D7093e069"
        if not contract_address:
            raise ValueError("KYC_ADDRESS is not set in the environment variables.")
        
        # Return a Web3 contract instance
        return w3.eth.contract(address=contract_address, abi=abi)
    except FileNotFoundError:
        raise FileNotFoundError("The ABI file 'KYC.json' was not found.")
    except Exception as e:
        raise RuntimeError(f"Error initializing contract: {e}")

def convertDataToJSON(first_name, last_name, dob, email, nationality, occupation, annual_income, image):
    """
    Convert KYC data into a JSON object suitable for uploading to Pinata.
    """
    try:
        data = {
            "pinataOptions": {"cidVersion": 1},
            "pinataContent": {
                "name": "KYC Report",
                "first_name": first_name,
                "last_name": last_name,
                "date_of_birth": dob,
                "email": email,
                "nationality": nationality,
                "occupation": occupation,
                "annual_income": annual_income,
                "image": image,
            },
        }
        return json.dumps(data)
    except Exception as e:
        raise ValueError(f"Error converting data to JSON: {e}")

def pinJSONtoIPFS(json_data):
    """
    Pin a JSON object to IPFS using Pinata's API and return the IPFS URI.
    """
    try:
        # Ensure json_data is a string (if it's not already)
        if isinstance(json_data, dict):
            json_data = json.dumps(json_data)
        
        response = requests.post(
            "https://api.pinata.cloud/pinning/pinJSONToIPFS", 
            data=json_data, 
            headers=headers
        )
        response.raise_for_status()  # Raise an error for bad responses
        ipfs_hash = response.json().get("IpfsHash")
        if not ipfs_hash:
            raise ValueError("Failed to retrieve IPFS hash from Pinata response.")
        return f"ipfs://{ipfs_hash}"
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error connecting to Pinata API: {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error during IPFS upload: {e}")

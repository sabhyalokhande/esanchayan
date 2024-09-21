from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your Pinata API key and secret
PINATA_API_KEY = '57033787091de4e779e6'
PINATA_API_SECRET = '96d14352187fcc49d6acc76a97a3551285066f4490c816f3e48b2ca4dd568a42'

@app.route('/upload', methods=['POST'])
def upload_to_ipfs():
    file = request.files['file']

    if file:
        # Set your Pinata API key and secret
        headers = {
            'pinata_api_key': PINATA_API_KEY,
            'pinata_secret_api_key': PINATA_API_SECRET,
        }

        # Upload the file to IPFS via Pinata
        response = requests.post('https://api.pinata.cloud/pinning/pinFileToIPFS', files={'file': (file.filename, file)}, headers=headers)

        if response.status_code == 200:
            ipfs_hash = response.json()['IpfsHash']
            return jsonify({'ipfsHash': ipfs_hash})
        else:
            return jsonify({'error': 'Error uploading the file to IPFS via Pinata'}), 500

    return jsonify({'error': 'No file provided'}), 400

@app.route('/')
def index():
    return open('documents.html').read()   

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
mediator_url = "http://localhost:8080"
server_id = 4  # New server ID for the message handler

@app.route('/forward_message', methods=['POST'])
def forward_message():
    data = request.get_json()
    destination_server_id = data.get('destination')
    message = data.get('message')

    if destination_server_id and message:
        # Get the address of the destination server from the mediator
        destination_address = requests.get(f"{mediator_url}/get_address/{destination_server_id}").json().get('address')

        if destination_address:
            # Forward the message to the destination server
            response = requests.post(f"{destination_address}/receive_message", json={"message": message})
            return jsonify({"status": "success", "response": response.text})
        else:
            return jsonify({"status": "error", "message": f"Destination server {destination_server_id} not found"})
    else:
        return jsonify({"status": "error", "message": "Invalid data"})

if __name__ == '__main__':
    app.run(port=1111) 
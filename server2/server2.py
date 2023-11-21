from flask import Flask, request, jsonify
import requests
import time
import os
from threading import Thread

app = Flask(__name__)
mediator_url = os.environ.get("MEDIATOR_URL","http://localhost:8080")
server_id = 2

def send_pong():
    while True:
        time.sleep(0.5)
        try:
            address = requests.get(f"{mediator_url}/get_address/{server_id}").json().get('address')
            if address:
                response = requests.get(f"{address}/ping")
                print(f"Server {server_id} received ping from Server 1:", response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error sending pong from Server {server_id}:", e)

@app.route('/ping')
def ping():
    return "ping"

if __name__ == '__main__':
    # Register the address with the mediator
    requests.post(f"{mediator_url}/register", json={"id": server_id, "address": f"http://localhost:5372"})
    
    pong_thread = Thread(target=send_pong)
    pong_thread.start()
    
    app.run(port=5372)

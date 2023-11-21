from flask import Flask, request, jsonify
import requests
import time
import os
from threading import Thread

app = Flask(__name__)
mediator_url = os.environ.get("MEDIATOR_URL","http://localhost:8080")
server_id = 1

def send_ping():
    while True:
        time.sleep(0.5)
        try:
            address = requests.get(f"{mediator_url}/get_address/{server_id}").json().get('address')
            if address:
                #print(f"Server {server_id} address obtained from mediator: {address}")
                response = requests.get(f"{address}/pong")
                print(f"Server {server_id} received pong from Server 2:", response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error sending ping from Server {server_id}:", e)

@app.route('/pong')
def pong():
    return "pong"

if __name__ == '__main__':
    # Register the address with the mediator
    requests.post(f"{mediator_url}/register", json={"id": server_id, "address": f"http://localhost:4567"})
    
    ping_thread = Thread(target=send_ping)
    ping_thread.start()
    
    app.run(port=4567)

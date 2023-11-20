from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
server3_url = "http://localhost:9090"  # Assuming Server 3 runs on port 9090

def get_server2_address():
    response = requests.get(server3_url + "/get_address/server2")
    return response.json()["address"]

def send_ping():
    server2_url = get_server2_address()

    while True:
        time.sleep(0.5)
        try:
            response = requests.get(server2_url + "/ping")
            print("Server 1 received ping from Server 2:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error sending ping:", e)

def register_with_server3():
    my_address = "http://localhost:4567"  # Adjust the port as needed
    requests.post(server3_url + "/register", json={"server": "server1", "address": my_address})

@app.route('/pong')
def pong():
    return "pong"

if __name__ == '__main__':
    ping_thread = Thread(target=send_ping)
    ping_thread.start()

    register_with_server3()  # Register with Server 3
    app.run(port=4567)

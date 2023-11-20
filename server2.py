from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
server3_url = "http://localhost:9090"  # Assuming Server 3 runs on port 9090

def get_server1_address():
    response = requests.get(server3_url + "/get_address/server1")
    return response.json()["address"]

def send_pong():
    server1_url = get_server1_address()

    while True:
        time.sleep(0.5)
        try:
            response = requests.get(server1_url + "/pong")
            print("Server 2 received pong from Server 1:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error sending pong:", e)

def register_with_server3():
    my_address = "http://localhost:5372"  # Adjust the port as needed
    requests.post(server3_url + "/register", json={"server": "server2", "address": my_address})

@app.route('/ping')
def ping():
    return "ping"

if __name__ == '__main__':
    pong_thread = Thread(target=send_pong)
    pong_thread.start()

    register_with_server3()  # Register with Server 3
    app.run(port=5372)

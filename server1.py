from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
directory_server_url = "http://localhost:8080"

def get_server2_address():
    response = requests.get(directory_server_url + "/server2")
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

@app.route('/pong')
def pong():
    return "pong"

if __name__ == '__main__':
    ping_thread = Thread(target=send_ping)
    ping_thread.start()

    app.run(port=4567)
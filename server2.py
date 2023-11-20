from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
directory_server_url = "http://localhost:8080"

def get_server1_address():
    response = requests.get(directory_server_url + "/server1")
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

@app.route('/ping')
def ping():
    return "ping"

if __name__ == '__main__':
    pong_thread = Thread(target=send_pong)
    pong_thread.start()

    app.run(port=5372)
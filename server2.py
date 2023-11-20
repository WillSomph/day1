from flask import Flask
import requests
import time
from threading import Thread

app = Flask(__name__)
server1_url = "http://localhost:4567"

def send_pong():
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

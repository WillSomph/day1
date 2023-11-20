from flask import Flask, jsonify

app = Flask(__name__)

servers = {
    "Server1": "http://localhost:4567",
    "Server2": "http://localhost:5372"
}

@app.route('/<server_name>')
def get_server_address(server_name):
    return jsonify({"address": servers.get(server_name, None)})

if __name__ == '__main__':
    app.run(port=8080)
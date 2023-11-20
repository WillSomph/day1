from flask import Flask, request
import json

app = Flask(__name__)
registered_servers = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    server_name = data.get('server')
    server_address = data.get('address')

    if server_name and server_address:
        registered_servers[server_name] = server_address
        print(f"Registered {server_name} at {server_address}")
        return "Registration successful", 200
    else:
        return "Invalid registration data", 400

@app.route('/get_address/<server_name>', methods=['GET'])
def get_address(server_name):
    return json.dumps({"address": registered_servers.get(server_name, "")})

if __name__ == '__main__':
    app.run(port=9090)

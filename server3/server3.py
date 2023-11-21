from flask import Flask, request, jsonify

app = Flask(__name__)
servers = {}  # Dictionnaire pour stocker les adresses des serveurs

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    server_id = data.get('id')
    server_address = data.get('address')

    if server_id and server_address:
        servers[server_id] = server_address
        print(f"Server {server_id} registered with address {server_address}")
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Invalid data"})

@app.route('/get_address/<int:server_id>')
def get_address(server_id):
    address = servers.get(server_id)
    return jsonify({"address": address})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

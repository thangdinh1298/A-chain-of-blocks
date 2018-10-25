from flask import Flask, jsonify, request
import requests
app = Flask(__name__)

connected_ports = [8080]

l = []

@app.route("/")
def index():
    return jsonify(l)

@app.route("/add_name", methods=['POST'])
def add_name():
    l.append(request.get_json()['name'])
    print(l)
    return jsonify(l)

@app.route("/post", methods=['POST'])
def request_to_post():
    r = requests.post("http://localhost:{}/add_name".
        format(connected_ports[0]), json=request.get_json())
    return str(r.status_code)
    
@app.route("/add_ports/<int:port>")
def add_port(port):
    connected_ports.append(port)
    return jsonify(connected_ports)

# if __name__ == '__main__':
#     app.run(debug=True)
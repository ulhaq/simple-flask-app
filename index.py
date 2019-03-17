from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    SERVER_PASSWORD = '11749'

    data = request.get_json()

    if data['client_password'] == SERVER_PASSWORD:
        return Response('{"success": "true"}', status=200, mimetype='application/json')
    else:
        return Response('{"success": "false"}', status=403, mimetype='application/json')

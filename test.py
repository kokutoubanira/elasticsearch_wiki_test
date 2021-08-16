from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', )
def hello():
    return jsonify({'message': 'hello internal'}), 200

app.run()





import requests
import json
response = requests.post(
    'http://localhost:8065/hooks/paa19k5s9jdamkdfmua9id7ihr', 
    data=json.dumps({
        'text': 'this is sample bot'
        }))

print(response.status_code)    # HTTPのステータスコード取得

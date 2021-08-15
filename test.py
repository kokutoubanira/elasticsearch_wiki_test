import requests
import json
response = requests.post(
    'http://localhost:8065/hooks/paa19k5s9jdamkdfmua9id7ihr', 
    data=json.dumps({
        'text': 'this is sample bot'
        }))

print(response.status_code)    # HTTPのステータスコード取得

from flask import Flask, request
import urllib2
import json

app = Flask('bootcamp-app') 

//Not sure if I need these next two lines here, or if I need to integrate the below the @app.route
req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)

@app.route('/iss', methods=['GET', 'POST'])
def iss():

    body = request.values['Body']
    response = requests.get('http://api.openweathermap.org/data/2.5/weather')
    
    obj = json.loads(response.read())

print obj['timestamp']
print obj['iss_position']['latitude'], obj['data']['iss_position']['latitude']

    return '<?xml version="1.0" encoding="UTF-8"?><Response><Message>' +str(timestamp) + '</Message></Response>'
    
app.run(debug=True, host='0.0.0.0', port=8080)

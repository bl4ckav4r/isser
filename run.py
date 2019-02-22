from flask import Flask, request
from datetime import datetime
import urllib2
import json

app = Flask('bootcamp-app') 

@app.route('/iss', methods=['GET', 'POST'])
def iss():
    
    req = urllib2.Request("http://api.open-notify.org/iss-now.json")
    response = urllib2.urlopen(req)
    
    obj = json.loads(response.read())

    print obj['timestamp']
    print obj['iss_position']['latitude'], obj['iss_position']['longitude']

    timestamp = datetime.utcfromtimestamp(obj['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
    iss_position = obj['iss_position']
    latitude = obj['iss_position']['latitude']
    longitude = obj['iss_position']['longitude']
    
    googs = 'https://www.google.com/maps/search/?api=1&query=' + str(latitude) + ',' + str(longitude) 
    print(googs)
    return '<?xml version="1.0" encoding="UTF-8"?><Response><Message>Time of Ping (UTC): ' + str(timestamp) + '\n' +'Position of the ISS' +'\n' +str(latitude) +' Latitude' + '\n' +str(longitude) +' Longitude\n' + '</Message></Response>'
#    return '<?xml version="1.0" encoding="UTF-8"?><Response><Message>' +'Time of Ping ' +str(timestamp) + '\n' +'Position of the ISS' +'\n' +str(latitude) +' Latitude' + '\n' +str(longitude) +' Longitude' + '</Message></Response>'
#    return '<?xml version="1.0" encoding="UTF-8"?><Response><Message>'+ googs + '</Message></Response>'
    
app.run(debug=True, host='0.0.0.0', port=8080) 

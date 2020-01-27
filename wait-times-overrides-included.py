import requests,json
from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def hello():
    url = "https://api-qa.mspmac.org/qa1.0/security-checkpoint/currentstatuses/"

    headers = {    'Content-Type': "application/json"}

    response = requests.request("GET", url, headers=headers)
    r_json = response.json()
    over_ride_locations = {}
    for r in r_json:
        if r['useSystemWaitTime'] is False and len(r['customWaitTime']) > 0:
            print(r['locationId'], r['location'], r['useSystemWaitTime'], r['customWaitTime'])
            over_ride_locations[str(r['location']).upper()] = r['customWaitTime']
    print(over_ride_locations)

    url = "https://api-qa.mspmac.org/qa1.0/security-checkpoint/waittimedisplays/"

    headers = {'Content-Type': "application/json"}

    response = requests.request("GET", url, headers=headers)
    r_json = response.json()
    if over_ride_locations:
        for over_ride in over_ride_locations:
            for loc in r_json:
                print("loc: ",  loc['location'], "  over_ride: ", over_ride)
                if(over_ride == loc['location']):
                    loc['wait_time_display'] = over_ride_locations[over_ride]
    print(r_json)
    app_response  = json.dumps(r_json)
    return Response(app_response, mimetype='application/json')
    # return "yo"
if __name__ == "__main__":
    app.run()

import requests,time
import datetime,json,random,time
from influxdb import InfluxDBClient


while(True):
    def save_to_influx(json_body):
        client = InfluxDBClient('localhost', 8086, 'root', 'root', 'prod-parking')
        client.write_points(json_body)
        result = client.query('select status from runways;')
        print("Result: {0}".format(result))


    def format_json(measurement,response_time, status):
        formatted_json =  [
            {
                "measurement": measurement,"tags": {},
                "time": str(datetime.datetime.utcnow()),
                "fields": {
                    "status": int(status),
                    "response_time": float(response_time)
                }
            }
        ]
        # print(formatted_json)
        return formatted_json

    wierd_urls = ["http://fs.mspmac.org/adfs/ls"] # does not return anything in postman
    # urls = [("https://api.macnoms.com/api/ft/runways/", "runways")]
    urls = [
    ("https://api.macnoms.com/api/ft/runways/","runways"),
    ("https://api-qa.mspmac.org/qa1.0/security-checkpoint/waittimedisplays","security-checkpoint"),
    ("https://myinfo.mspairport.com","myinfo"),
    ("https://ecp.macenvironment.org","macenvironment-ecp"),
    #("https://gis.mspmac.org/portal/home/","gis"),
    ("http://www.macenvironment.org","macenvironment"),
    ("https://www.macnoise.com/","macnoise"),
    ("https://macnoms.com","macnoms"),
    ("http://www.metroairports.org","metroairports"),
    ("http://www.mspairport.com","mspairport"),
    ("https://api.mspmac.org","api-mspmac"),
    ("https://mac.certpointsystems.com/Portal/Login.aspx","certpointsystems"),
    ("https://sft.mspairport.com","sft"),
    ("http://tncpermit.mspmac.org","tncpremit"),
    ("https://remote.mspairport.com","remote-vpn"),
    ("http://xovis.mspmac.org","xovis"),
    ("http://onlineparking.mspmac.org","onlineparking-org"),
    ("http://onlineparking.mspairport.com","onlineparking-com"),
    ("https://api.mspmac.org/PreBooking?wsdl","prebooking"),
	("https://wfdirector.logis.org/MAC/login.aspx","wfdirector")
    ]

    no_auth_sites = ["http://xovis.mspmac.org"]

    for url in urls:
        headers = {
            'Content-Type': "application/json",
            'Authorization': "token-here",
            'Cache-Control': "no-cache",
            'Postman-Token': "0ec18eab-b8dc-7c64-93fc-2455b74ed5ea"
            }
        if url[0] in no_auth_sites:
            del headers['Authorization']
        response = requests.request("GET", url[0], headers=headers)
        response_time = response.elapsed.total_seconds()
        status_code = int(response.status_code)
        status = 1 if status_code == 200 else 0
        json_body = format_json(url[1], response_time, status)
        save_to_influx(json_body)
        print(status_code,status,response_time,url)
    time.sleep( 60 )


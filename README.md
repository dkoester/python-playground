# python-playground
Store some helpful scripts! Hoping others find this useful!


#### pull_all_repos.py
This file helps pull all the repos under the mac git org. It requires your oath token to be used. It is limited to 100 repos per request so you might have to change/modify the output to fit your needs. Here is the basic cURL used in the request
```
curl -X GET \
  'https://api.github.com/orgs/mspmac/repos?access_token=token-here&per_page=200&page=3' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 03fccae9-cfb0-c719-dc23-d9139e42afa4'
```

#### wait-times 
This is a Flask based script that runs on local host to check the current wait times and then override anything returned on the currentstatuses API for inflight overrides.

#### msp-watch 
This is meant to be used as a site monitoring tool to hit specific urls at scheduled intervals and publish the data into influxDB to be graphed with grafana locally on the server and rules are created to sent messages to #apollo-en-fuego

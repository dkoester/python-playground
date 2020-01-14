# python-playground
Store some helpful scripts!


#### pull_all_repos.py
This file helps pull all the repos under the mac git org. It requires your oath token to be used. It is limited to 100 repos per request so you might have to change/modify the output to fit your needs. Here is the basic cURL used in the request
```
curl -X GET \
  'https://api.github.com/orgs/mspmac/repos?access_token=token-here&per_page=200&page=3' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 03fccae9-cfb0-c719-dc23-d9139e42afa4'
```

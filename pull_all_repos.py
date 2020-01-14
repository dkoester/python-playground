import requests,csv

url = "https://api.github.com/orgs/mspmac/repos"

querystring = {"access_token":"token-here", "per_page":"200", "page":"1"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "665d9900-d33c-3238-281e-34baa3b083e0"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
r_json = response.json()
# for r in r_json:
#     print("git clone " + r['html_url'])
git_data = open('git-data.csv','w')
csvwriter = csv.writer(git_data)
headers = {"App":"","description":"" ,"url":"", "criticality":""}
csvwriter.writerow(headers.keys())
for r in r_json:
    csvwriter.writerow([r['name'], r['description'], r['html_url'], ""])

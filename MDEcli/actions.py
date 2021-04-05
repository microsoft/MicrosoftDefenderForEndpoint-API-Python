import json
import urllib.request
import urllib.parse
import csv
import login

class Action:

    def __init__(self, tenantId, appId, appSecret, body, url, filename, column):
        self.tenantId = tenantId
        self.appId = appId
        self.appSecret = appSecret
        self.body = body
        self.url = url
        self.filename = filename
        self.column = column

    def action(self):
        login_MDEcli = login.Login(self.tenantId, self.appId, self.appSecret)
        aadToken = login_MDEcli.login()

        with open(self.filename, newline='') as csvfile:
            data = csv.DictReader(csvfile)
            for item in data:
                try:
                    url = f"https://api.securitycenter.microsoft.com/api/machines/{item[self.column].strip()}/{self.url}"
                    headers = { 
                        'Content-Type' : 'application/json',
                        'Accept' : 'application/json',
                        'Authorization' : "Bearer " + aadToken
                    }

                    data = str(json.dumps(self.body)).encode("utf-8")

                    req = urllib.request.Request(url=url, data=data, headers=headers)
                    response = urllib.request.urlopen(req)
                    jsonResponse = json.loads(response.read())
                    
                    computerDnsName = jsonResponse['computerDnsName']
                    print(f'{self.url} started on {computerDnsName}')

                except Exception as e:
                    print(f'Someting went wrong:{e}')
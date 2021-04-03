import json
import urllib.request
import urllib.parse
import csv
import login

class List:

    def __init__(self, tenantId, appId, appSecret, urlpart, filename):
        self.tenantId = tenantId
        self.appId = appId
        self.appSecret = appSecret
        self.urlpart = urlpart
        self.filename = filename
    
    def list(self):
            login_MDEcli = login.Login(self.tenantId, self.appId, self.appSecret)
            aadToken = login_MDEcli.login()

            url = f"https://api.securitycenter.microsoft.com/api/{self.urlpart}"
            headers = { 
                'Content-Type' : 'application/json',
                'Accept' : 'application/json',
                'Authorization' : "Bearer " + aadToken
            }

            req = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(req)
            jsonResponse = json.loads(response.read())

            # Empty results
            if not jsonResponse['value']:
                print('Nothing done.')
            
            else:
                # CSV & print        
                fields = jsonResponse['value'][0].keys()

                with open(self.filename, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames = fields)
                    writer.writeheader()
                    writer.writerows(jsonResponse['value'])
                
                for index, item in enumerate(jsonResponse['value']):
                    print('\n')
                    print(item)
                
                print(f'\nFull results can be imported to PowerBI from {self.filename}\n')
    
    def list_no_csv(self):
        login_MDEcli = login.Login(self.tenantId, self.appId, self.appSecret)
        aadToken = login_MDEcli.login()

        url = f"https://api.securitycenter.microsoft.com/api/{self.urlpart}"
        headers = { 
            'Content-Type' : 'application/json',
            'Accept' : 'application/json',
            'Authorization' : "Bearer " + aadToken
        }

        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req)
        jsonResponse = json.loads(response.read())

        # Empty results
        if not jsonResponse['value']:
            print('Nothing done.')
        
        else:
            print('\n')
            for item in jsonResponse.items():
                print(item)
        print('\n')

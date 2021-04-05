import json
import urllib.request
import urllib.parse

class Login:

    def __init__(self, tenantId, appId, appSecret):
        self.tenantId = tenantId
        self.appId = appId
        self.appSecret = appSecret

    def login(self):
     
        url = "https://login.windows.net/%s/oauth2/token" % (self.tenantId)

        resourceAppIdUri = 'https://api.securitycenter.windows.com'

        body = {
            'resource' : resourceAppIdUri,
            'client_id' : self.appId,
            'client_secret' : self.appSecret,
            'grant_type' : 'client_credentials'
        }

        data = urllib.parse.urlencode(body).encode("utf-8")

        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        jsonResponse = json.loads(response.read())
        aadToken = jsonResponse["access_token"]
        return aadToken

#!/usr/bin/python3
import json
import urllib.request
import urllib.parse
import sys
from datetime import datetime, timedelta

#Returns the AAD token
def get_aadToken():
    tenantId = "<Paste Tenant ID here>"            
    appId = "<Paste Application ID here>"               
    appSecret = "<Paste Application Key (Application Secret)>"

    url = "https://login.windows.net/%s/oauth2/token" % (tenantId)
    resourceAppIdUri = 'https://api.securitycenter.windows.com'
    body = {
        'resource' : resourceAppIdUri,
        'client_id' : appId,
        'client_secret' : appSecret,
        'grant_type' : 'client_credentials'
    }

    data = urllib.parse.urlencode(body).encode("utf-8")
    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    jsonResponse = json.loads(response.read())
    aadToken = jsonResponse["access_token"]
    return aadToken

#Kill the script if the isolation type isn't valid
def validate_isolationType(type):
    if(isolation_type!="Full" and isolation_type!="Selective"):
        print("Invalid isolation type (can be either Full or Selective)")
        print("script failed")
        exit(1)

#Isolate a specific machine specified by the machine_id
def mdatp_isolate_machine(aadToken, machine_id, comment, isolation_type):
    url = "https://api.securitycenter.windows.com/api/machines/{}/isolate".format(machine_id)
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : "Bearer " + aadToken
    }
    
    body = {
        'Comment' : comment,
        'IsolationType' : isolation_type
    }
    data = str(json.dumps(body)).encode("utf-8")
    req = urllib.request.Request(url=url,data=data,headers=headers)
    response = urllib.request.urlopen(req)
    jsonResponse = json.loads(response.read())
    return jsonResponse["status"]

#Isolate every machine with High proiroty alert inthe previous hour
def mdatp_isolate_high_severity_machines(aadToken, comment, isolation_type):
    #build get-alerts API
    filterTime = datetime.now() - timedelta(hours = 1)          #If you want to include alerts from longer then an hour, change here (days, weeks)
    filterTime = filterTime.strftime("%Y-%m-%dT%H:%M:%SZ")
    url = "https://api.securitycenter.windows.com/api/alerts?$filter=alertCreationTime+ge+{}+and+severity+eq+'High'".format(filterTime)
    headers = {
        'Content-Type' : 'application/json',
        'Accept' : 'application/json',
        'Authorization' : "Bearer " + aadToken
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    jsonResponse = json.loads(response.read())
    #For each alert, isolate the machine
    for alert in jsonResponse["value"]:
        machineId = alert["machineId"]
        alertId = alert["id"]
        response = mdatp_isolate_machine(aadToken, machineId, comment, isolation_type)
        if(response == "InProgress"):
            print("Machine {} isolated due to alert {}".format(machineId, alertId))
        else:
            print("Failed to isolate machine {}, status: ".format(machineId) + response)

if __name__ == '__main__':
    aadToken = get_aadToken()
    if(len(sys.argv)==4):
        #User input: MachineId, Comment, IsolationType.
        #Action: Isolate specific machine
        machine_id = sys.argv[1]
        comment = sys.argv[2]
        isolation_type = sys.argv[3]
        validate_isolationType(isolation_type)
        response = mdatp_isolate_machine(aadToken,machine_id,comment,isolation_type)
        if(response == "InProgress"):
            print("Machine isolated succesfully")
        else:
            print("Isolation failed, status: " + response)
    elif(len(sys.argv)==3):
        #User input: Comment, IsolationType.
        #Action: Isolate machines with a 'High' severity alert in the past hour
        comment = sys.argv[1]
        isolation_type = sys.argv[2]
        validate_isolationType(isolation_type)
        mdatp_isolate_high_severity_machines(aadToken, comment, isolation_type)
    else:
        print("Please provide the following arguments: comment, isolation type (Full or Selective)")
        print("For isolating a single machine by machineID provide the following arguments: machineID, comment, isolation type (Full or Selective)")
        print("Script failed")
        exit(1)
    

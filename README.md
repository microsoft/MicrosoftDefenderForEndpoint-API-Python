---
page_type: sample
languages:
- python
products:
- dotnet
description: "MDATP Python automation - Automate machine isolation with Python script"
---

# MDATP Python automation

In this blog, we will use Python (!) to automate a response to a high severity alert, by isolating the machine involved.

In a [previous blog](https://techcommunity.microsoft.com/t5/Microsoft-Defender-ATP/Automate-Windows-Defender-ATP-response-action-Machine-isolation/m-p/362701#M8), we provided a PowerShell script with the same functionality. Due to several requests we want to demonstrate the same with Python as well.

* Step 1: Add the required permission to your application

* Step 2: Download the script and insert your credentials

* Step 3: Run the script and bask in automation glory

## Step 1 - Add the required permission to the application:

If you’ve already created an app, you can skip and move to the “add isolation permissions” section below. If you haven’t, first you need to create one using the instructions described in the first part of the [Hello world](https://techcommunity.microsoft.com/t5/Microsoft-Defender-ATP/WDATP-API-Hello-World-or-using-a-simple-PowerShell-script-to/ba-p/326813) blog, and then move on to "add isolation permissions".

Please save your **Application key, Application ID and Tenant ID** while you create your app, you will use them soon (instructions on where to find this are in the blog linked above).

### Add isolation permissions:

* Open [Azure portal](https://ms.portal.azure.com/#home)
* Navigate to Azure Active Directory > App registrations 
* Under All Apps, find and select the application, for example ContosoSIEMConnector 
* Click on View API Permissions > then Add a permission
* Select the checkbox for Isolate machine application permission (make sure you have the “read alerts” permission as well).

![azure portal steps](https://gxcuf89792.i.lithium.com/t5/image/serverpage/image-id/116951i8BDE7C044918D123/image-size/large?v=1.0&px=999)

* Click Save and Grant Permissions. 
* Click on Grant admin consent. Make sure that the new permissions have admin consent as seen below (Read all alerts & Isolate machine).
![grant admin consent](https://gxcuf89792.i.lithium.com/t5/image/serverpage/image-id/116955i429996F533E0E10F/image-size/large?v=1.0&px=999)
Done! You have successfully added the required permissions to the application.

## Step 2: copy the script and insert your credentials
Copy the content of the isolation.py file from this repository to your own python (.py) file.

Remember when I asked you to save your **Application key, Application ID and Tenant ID** from the azure portal? We will now *embed them into the script*. 

Paste the values as strings (between a pair of quotation marks) here (line 9):
![past here](https://gxcuf89792.i.lithium.com/t5/image/serverpage/image-id/117019i025518DC7FA5C64B/image-size/large?v=1.0&px=999)
This will allow the script to use the API freely, so you won’t have to pass those values every time you run it.

## Step 3: Run the script

Open Powershell, go to the *directory you saved your file in* and run the following command:

```
Python isolation.py “Comment regarding the isolation” Full
```

***That’s it! You are DONE!***

The script will print out the MachineID of the isolated machines and the AlertID of the alert that triggered the isolation.

The arguments that are passed to the script are:

| **Parameter**     | **Type**   | **Description**                                                                  |
|-------------------|------------|----------------------------------------------------------------------------------|
| Comment           | String     | Comment to associate with the action. **Required.**                              |
| IsolationType     | String     | Type of the isolation. Allowed values are: 'Full' or 'Selective'. **Required.**  |

You can read more about our API in [this link](https://docs.microsoft.com/en-gb/windows/security/threat-protection/microsoft-defender-atp/exposed-apis-list).

## Bonus step: Isolate a single machine using MachineID

This script can also isolate a single machine, you simply need to provide the the ID of this machine. You can find the MachineID in the URL of the machine page in the security center:
![machine ID in URL](https://gxcuf89792.i.lithium.com/t5/image/serverpage/image-id/116960i82E37B1017B4CC3D/image-size/large?v=1.0&px=999)
Now, simply run the script, same as before, but pass the MachineID as the first argument as follows:
```
Python isolation.py 31bf22448170e3df65430b81fff82fbb30285cec “Comment regarding the isolation” Full
```

The rest of the arguments are the same as above.

**You can use this functionality to build more (exciting) automations!**

 
As always, we would love to get your thoughts and feedback.

Thanks,

@Itai Zur, program manager, Windows Defender ATP

@Dan Michelson, program manager, Windows Defender ATP

@Haim Goldshtein, security software engineer, Windows Defender ATP


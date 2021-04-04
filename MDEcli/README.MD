# MDEcli
![image](https://user-images.githubusercontent.com/76814237/113495471-f72acc00-94e9-11eb-93de-e04472ed066c.png)
## About
MDEcli is a Microsoft Defender Endpoint (MDE) enhancer allowing organizations to use the advanced features of the MDE API to achieve more faster. This tool, fully developed in Python aims to allow organizations to perform tasks on multiple machines in a easy and fast way. Built on the API structure above, organizations can leverage the power MDE with the reach and flexibility of the API. This tool also generates CSV files (from --list subcommand) that can be worked in Excel or imported directly to PowerBI.
## Config
To use MDEcli you'll need to create an Application Registration on your Azure tenant. Since this tool is fully integrated, be sure to allow enough permissions to WindowsDefenderATP from App Registartion.
## Usage
Please use help to understand the structure of commands and subcommands. Subcommands, specially when using "machine-actions", they require user to input a filename (CSV format) and a column, can be leverage by using the CSV files created with any "--list" subcommand. Just make sure you identify the proper column with the information required.
## Help
On PS or CMD:
````
MDEcli.exe -h

usage: MDEcli.exe [-h] {alerts,machine,machine-actions,automated-investigations,indicators,score,software,vulnerabilities,recomendations} ...

optional arguments:
  -h, --help            show this help message and exit

Commands:
  {alerts,machine,machine-actions,automated-investigations,indicators,score,software,vulnerabilities,recomendations}
                        Choose one of the main options. MDEcli -<option> -h for more details for each main option.
    alerts              Alert resource type
    machine             Machine resource type
    machine-actions     MachineAction resource type
    automated-investigations
                        Investigation resource type
    indicators          Indicator resource type
    score               Score resource type
    software            Software resource type
    vulnerabilities     Vulnerability resource type
    recomendations      Recommendation resource type
````

For help inside main category, for example:
````
MDEcli.exe machine-actions -h

usage: MDEcli.exe machine-actions [-h] [--list] [--collect] [--full-isolate] [--selective-isolate] [--unisolate] [--restrict-app-execution] [--unrestrict-app-execution] [--quick] [--full] [--offboard] [--quarantine]

optional arguments:
  -h, --help            show this help message and exit
  --list                Retrieves a collection of Machine Actions
  --collect             Collect investigation package from a device.
  --full-isolate        Fully isolates a device from accessing external network.
  --selective-isolate   Restrict only limited set of applications from accessing the network.
  --unisolate           Undo isolation of a device.
  --restrict-app-execution
                        Restrict execution of all applications on the device except a predefined set.
  --unrestrict-app-execution
                        Enable execution of any application on the device.
  --quick               Initiate Microsoft Defender Antivirus quick scan on a device.
  --full                Initiate Microsoft Defender Antivirus full scan on a device.
  --offboard            Offboard device from Defender for Endpoint.
  --quarantine          Stop execution of a file on a device and delete it.
## Latest version
https://aka.ms/MDEcli
````
## To-Do
- Get authentication to use session instead authenticate everytime
- Integrate "GET" API functions:
  - Alert
  - Machine
  - Machine Action
  - Automated Investigations
  - Indicators
  - Domain
  - File
  - IP
  - User
  - Score
  - Software
  - Vulnerability (pending internal fix)
  - Recomendation

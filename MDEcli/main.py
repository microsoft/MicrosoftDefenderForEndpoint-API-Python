import sys
import getpass
import argparse
import list

# Menu
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='Commands', title='Commands', help='Choose one of the main options. MDEcli -<option> -h for more details for each main option.')
subparsers.required=True

#Alerts Menu
alertsparser = subparsers.add_parser('alerts', help='Alert resource type')
alertsparser.add_argument('--list', help='Retrieves a collection of Alerts', action='store_true')

#Machine Menu
machinesparser = subparsers.add_parser('machine', help='Machine resource type')
machinesparser.add_argument('--list', help='Retrieves a collection of Machines that have communicated with Microsoft Defender for Endpoint cloud', action='store_true')

#Machines Actions menu
machineactionsparser = subparsers.add_parser('machine-actions', help='MachineAction resource type')
machineactionsparser.add_argument('--list', help='Retrieves a collection of Machine Actions', action='store_true')

#Automated Investigations menu
automatedinvestigationsparser = subparsers.add_parser('automated-investigations', help='Investigation resource type')
automatedinvestigationsparser.add_argument('--list', help='Retrieves a collection of Investigations', action='store_true')

#Indicators menu
indicatorsparser = subparsers.add_parser('indicators', help='Indicator resource type')
indicatorsparser.add_argument('--list', help='Retrieves a collection of all active Indicators', action='store_true')

#Score menu
scoreparser = subparsers.add_parser('score', help='Score resource type')
scoreparser.add_argument('--list', help='Retrieves a list of exposure score per device group', action='store_true')

#Software menu
softwareparser = subparsers.add_parser('software', help='Software resource type')
softwareparser.add_argument('--list', help='Retrieves the organization software inventory', action='store_true')

#Vulnerability menu
vulnerabilityparser = subparsers.add_parser('vulnerabilities', help='Vulnerability resource type')
vulnerabilityparser.add_argument('--list', help='Retrieves a list of all the vulnerabilities affecting the organization', action='store_true')

#Recomendations menu
recomendationsparser = subparsers.add_parser('recomendations', help='Recommendation resource type')
recomendationsparser.add_argument('--list', help='Retrieves a list of all security recommendations affecting the organization', action='store_true')

if len(sys.argv) <= 1:
    sys.argv.append('--help')

args = parser.parse_args()

# Alerts
if args.Commands == 'alerts':  
    if args.list:
        tenantId = input('Enter your Tenant ID: ')
        appId = input('Enter your application ID: ')
        appSecret = getpass.getpass('Enter your application Secret (does not show in cli): ')
        list_alerts = list.List(tenantId, appId, appSecret, 'alerts', 'alerts.csv')
        list_alerts.list()
    else:
        parser.print_help(sys.stderr)  

# Machine
elif args.Commands == 'machine':
    if args.list:
        tenantId = input('Enter your Tenant ID: ')
        appId = input('Enter your application ID: ')
        appSecret = getpass.getpass('Enter your application Secret (does not show in cli): ')
        list_machine = list.List(tenantId, appId, appSecret, 'machines', 'machines.csv')
        list_machine.list()
    else:
        parser.print_help(sys.stderr)

# Machine Actions
elif args.Commands == 'machine-actions':
    if args.list:
        tenantId = input('Enter your Tenant ID: ')
        appId = input('Enter your application ID: ')
        appSecret = getpass.getpass('Enter your application Secret (does not show in cli): ')
        list_machine_actions = list.List(tenantId, appId, appSecret, 'machineactions', 'machineactions.csv')
        list_machine_actions.list()
    else:
        parser.print_help(sys.stderr)

# Automated Investigations --> requires checking
elif args.Commands == 'automated-investigations':
    if args.list:
        tenantId = input('Enter your Tenant ID: ')
        appId = input('Enter your application ID: ')
        appSecret = getpass.getpass('Enter your application Secret (does not show in cli): ')
        list_automated_investigations = list.List(tenantId, appId, appSecret, 'investigations', 'investigations.csv')
        list_automated_investigations.list()
    else:
        parser.print_help(sys.stderr)

# Indicators
elif args.Commands == 'indicators':
    if args.list:
        tenantId = input('Enter your Tenant ID: ')
        appId = input('Enter your application ID: ')
        appSecret = getpass.getpass('Enter your application Secret (does not show in cli): ')
        list_indicators = list.List(tenantId, appId, appSecret, 'indicators', 'indicators.csv')
        list_indicators.list()
    else:
        parser.print_help(sys.stderr)

# Score --> requires checking
elif args.Commands == 'score':
    if args.list:
        tenantId = input('Enter your Tenant ID: ')
        appId = input('Enter your application ID: ')
        appSecret = getpass.getpass('Enter your application Secret (does not show in cli): ')
        list_score = list.List(tenantId, appId, appSecret, 'exposureScore', 'exposureScore.csv')
        list_score.list()
    else:
        parser.print_help(sys.stderr)

# Software
elif args.Commands == 'software':
    if args.list:
        tenantId = input('Enter your Tenant ID: ')
        appId = input('Enter your application ID: ')
        appSecret = getpass.getpass('Enter your application Secret (does not show in cli): ')
        list_software = list.List(tenantId, appId, appSecret, 'Software', 'Software.csv')
        list_software.list()
    else:
        parser.print_help(sys.stderr)

# Vulnerabilities --> NOT WORKING RETURNS ALL CVE's
#elif args.Commands == 'vulnerabilities':
#    if args.list:
#        tenantId = input('Enter your Tenant ID: ')
#        appId = input('Enter your application ID: ')
#        appSecret = getpass.getpass('Enter your application Secret (does not show in cli): ')
#        list_vulnerabilities = list.List(tenantId, appId, appSecret, 'vulnerabilities', 'vulnerabilities.csv')
#        list_vulnerabilities.list()
#    else:
#        parser.print_help(sys.stderr)

# Recomendations
elif args.Commands == 'recomendations':
    if args.list:
        tenantId = input('Enter your Tenant ID: ')
        appId = input('Enter your application ID: ')
        appSecret = getpass.getpass('Enter your application Secret (does not show in cli): ')
        list_recomendations = list.List(tenantId, appId, appSecret, 'recommendations', 'recommendations.csv')
        list_recomendations.list()
    else:
        parser.print_help(sys.stderr)
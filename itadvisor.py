import json
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class ITAdvisor:
    '''Initialize with hostname, username and password.'''

    def __init__(self, hostname, username, password):
        '''IT Advisor Complete REST API Library'''
        self.hostmame = hostname
        self.http_auth = HTTPBasicAuth(username, password)
        self.Assets = self.Assets(hostname = self.hostmame, http_auth = self.http_auth)
        self.AuditTrail = self.AuditTrail(hostname = self.hostmame, http_auth = self.http_auth)
        self.Authentication = self.Authentication(hostname = self.hostmame, http_auth = self.http_auth)
        self.AuthenticationServers = self.AuthenticationServers(hostname = self.hostmame, http_auth = self.http_auth)
        self.Backup = self.Backup(hostname = self.hostmame, http_auth = self.http_auth)
        self.Certificates = self.Certificates(hostname = self.hostmame, http_auth = self.http_auth)
        self.ChangeRequest = self.ChangeRequest(hostname = self.hostmame, http_auth = self.http_auth)
        self.ChangeRequestTemplate = self.ChangeRequestTemplate(hostname = self.hostmame, http_auth = self.http_auth)
        self.Configuration = self.Configuration(hostname = self.hostmame, http_auth = self.http_auth)
        self.CustomProperties = self.CustomProperties(hostname = self.hostmame, http_auth = self.http_auth)
        self.Customers = self.Customers(hostname = self.hostmame, http_auth = self.http_auth)
        self.CustomersCount = self.CustomersCount(hostname = self.hostmame, http_auth = self.http_auth)
        self.EquipmentBrowser = self.EquipmentBrowser(hostname = self.hostmame, http_auth = self.http_auth)
        self.ETLConfiguration = self.ETLConfiguration(hostname = self.hostmame, http_auth = self.http_auth)
        self.Genomes = self.Genomes(hostname = self.hostmame, http_auth = self.http_auth)
        self.KPIs = self.KPIs(hostname = self.hostmame, http_auth = self.http_auth)
        self.Licenses = self.Licenses(hostname = self.hostmame, http_auth = self.http_auth)
        self.Mail = self.Mail(hostname = self.hostmame, http_auth = self.http_auth)
        self.PlatformStatus = self.PlatformStatus(hostname = self.hostmame, http_auth = self.http_auth)
        self.PowerCapacity = self.PowerCapacity(hostname = self.hostmame, http_auth = self.http_auth)
        self.PowerPath = self.PowerPath(hostname = self.hostmame, http_auth = self.http_auth)
        self.SensorMapping = self.SensorMapping(hostname = self.hostmame, http_auth = self.http_auth)
        self.StruxureOn = self.StruxureOn(hostname = self.hostmame, http_auth = self.http_auth)
        self.SVG = self.SVG(hostname = self.hostmame, http_auth = self.http_auth)
        self.UserGroups = self.UserGroups(hostname = self.hostmame, http_auth = self.http_auth)
        self.UserMessage = self.UserMessage(hostname = self.hostmame, http_auth = self.http_auth)
        self.Users = self.Users(hostname = self.hostmame, http_auth = self.http_auth)
        self.WorkOrders = self.WorkOrders(hostname = self.hostmame, http_auth = self.http_auth)
        
    class Assets:
        '''Asset Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
            
        def Query(self, query):
            '''
            Searches for assets containing the words in the string.
            The search functionality is viable for searching specific rooms, locations or assets. 
            It is an indexed search, limited to 50 items. 
            It uses cashed data and may not represent the most recent changes in your datacenter
            '''
            requests.packages.urllib3.disable_warnings()
            url = "https://" +str(self.hostmame)+ "/api/current/assets/search?q=" + str(query)
            payload={}
            headers = {}
            try:
                response = requests.request("GET", url, headers=headers, data=payload, verify=False, auth=self.http_auth)
                if response.status_code != 200:
                    return response.status_code
                return response.text
            except requests.exceptions.ConnectionError:
                return '{\'status\':\'0\', \'description\':\'unreachable\'}'
        
    class AuditTrail:
        '''Audit Trail Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class Authentication:
        '''Authentication Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class AuthenticationServers:
        '''Authentication Server Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class Backup:
        '''Backup Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class Certificates:
        '''Certificate Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class ChangeRequest:
        '''Change Request Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class ChangeRequestTemplate:
        '''Change Request Template Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class Configuration:
        '''Configuration Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class CustomProperties:
        '''Custom Properties Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class Customers:
        '''Customers Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class CustomersCount:
        '''Customer Count Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class EquipmentBrowser:
        '''Equipment Browser Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class ETLConfiguration:
        '''ETL Configuration Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class Genomes:
        '''Genomes Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class KPIs:
        '''KPIs Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class Licenses:
        '''Licenses Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class Mail:
        '''Mail Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class PlatformStatus:
        '''Platform Status Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class PowerCapacity:
        '''Power Capacity Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class PowerPath:
        '''Power Path Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class SensorMapping:
        '''Sensor Mapping Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class StruxureOn:
        '''StruxureOn Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class SVG:
        '''SVG Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class UserGroups:
        '''User Groups Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class UserMessage:
        '''User Message Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class Users:
        '''Users Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth
        
    class WorkOrders:
        '''Work Orders Library'''
        def __init__(self, hostname, http_auth):
            '''init'''
            self.hostmame = hostname
            self.http_auth = http_auth

if __name__ == "__main__":
    print("Author: David Romero")
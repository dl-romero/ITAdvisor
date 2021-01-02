import requests
import json

class ITAdvisor:
    '''Initialize with hostname, username and password.'''

    def __init__(self, hostname, username, password):
        '''test'''
        self.hostmame = hostname
        self.username = username
        self.password = password
    
    def get_assets(self, asset):
        '''test'''
        print(asset)
        print(self.hostmame)
        print(self.username)
        print(self.password)
    
    def get_etl_status(self):
        '''test'''
        return True

    def get_group_permissions(self, group_name):
        '''test'''
        return True

    def get_user_permissions(self, user_name):
        '''test'''
        return True

    def generate_permissions_report(self, file_path, file_name):
        '''test'''
        return True

if __name__ == "__main__":
    ita = ITAdvisor(hostname = 'hostname', username = 'user', password = 'password')
    ita.get_assets("test")
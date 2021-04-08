import requests,json
from pycloudbasic.CloudBasicAuth import cloudBasicAuth as cba
from common import common as c

class multiazhacluster:
    def __init__(self,host,action,request_parameters,method=None):
        print("Multi-AZ HA Cluster Management Called")
        self.request_parameters = request_parameters
        content_type,amz_date,payload_hash,authorization_header = cba.createSignture(cba(method),host,action,self.request_parameters)
    
        self.headers = {'Content-Type':content_type,
        'X-Amz-Date':amz_date,
        'x-amz-content-sha256': payload_hash,
        'Authorization':authorization_header}


    def CreateCluster (self,endpoint):
        print("CreateCluster Called")
        '''
        https://cloudbasic.net/documentation/api/CreateCluster/
        '''
        print('Request URL = ' + endpoint)
        r = requests.get(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()


    def AlterCluster(self,endpoint):
        print("AlterCluster Called")
        '''
        https://cloudbasic.net/documentation/api/AlterCluster/
        '''
        print('Request URL = ' + endpoint)
        r = requests.get(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()

    def DeleteCluster(self,endpoint):
        print("DeleteCluster Called")
        '''
        https://cloudbasic.net/documentation/api/DeleteCluster/
        '''
        print('Request URL = ' + endpoint)
        r = requests.get(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()

    def PromoteDbReplicaToPrimary(self,endpoint):
        print("PromoteDbReplicaToPrimary Called")
        '''
        https://cloudbasic.net/documentation/api/PromoteDbReplicaToPrimary/
        '''
        print('Request URL = ' + endpoint)
        r = requests.get(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()

    def PromoteDbReplicaToPrimaryStatus(self,endpoint):
        print("PromoteDbReplicaToPrimaryStatus Called")
        '''
        https://cloudbasic.net/documentation/api/PromoteDbReplicaToPrimaryStatus/
        '''
        print('Request URL = ' + endpoint)
        r = requests.get(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()

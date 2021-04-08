import requests,json
from pycloudbasic.CloudBasicAuth import cloudBasicAuth as cba
from common import common as c

class sysMan:
    def __init__(self,host,action,request_parameters,method=None):
        print("System Wide Managment Called")
        self.request_parameters = request_parameters
        content_type,amz_date,payload_hash,authorization_header = cba.createSignture(cba(method),host,action,self.request_parameters)
    
        self.headers = {'Content-Type':content_type,
        'X-Amz-Date':amz_date,
        'x-amz-content-sha256': payload_hash,
        'Authorization':authorization_header}


    def ReplicationServiceStatus(self,endpoint):
        print("ReplicationServiceStatus Called")
        '''
        https://cloudbasic.net/documentation/api/replicationservicestatus/
        '''
        print('Request URL = ' + endpoint)
        r = requests.get(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()


    def StartReplicationService(self,endpoint):
        print("StartReplicationService Called")
        '''
        https://cloudbasic.net/documentation/api/StartReplicationService/
        '''
        print('Request URL = ' + endpoint)
        r = requests.get(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()

    def StopReplicationService(self,endpoint):
        print("StopReplicationService Called")
        '''
        https://cloudbasic.net/documentation/api/StopReplicationService/
        '''
        print('Request URL = ' + endpoint)
        r = requests.get(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()
    
    def ActivateActiveDirectory(self,endpoint):
        print("ActivateActiveDirectory Called")
        '''
        https://cloudbasic.net/documentation/api/activateactivedirectory/
        '''

    def DeactivateActiveDirectory(self,endpoint):
        print("DeactivateActiveDirectory Called")
        '''
        https://cloudbasic.net/documentation/api/deactivateactivedirectory/
        '''
    
    def ActiveDirectoryStatus(self,endpoint):
        print("ActiveDirectoryStatus Called")
        '''
        https://cloudbasic.net/documentation/api/ActiveDirectoryStatus/
        '''

    def CreateAndBindSelfSignedCertificate(self,endpoint):
        print("CreateAndBindSelfSignedCertificate Called")
        '''
        https://cloudbasic.net/documentation/api/createandbindselfsignedcertificate/
        '''

    def UnbindAndDeleteSelfSignedCertificate(self,endpoint):
        print("UnbindAndDeleteSelfSignedCertificate Called")
        '''
        https://cloudbasic.net/documentation/api/unbindanddeleteselfsignedcertificate/
        '''


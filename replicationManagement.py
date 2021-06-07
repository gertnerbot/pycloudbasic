import requests,json
from pycloudbasic.CloudBasicAuth import cloudBasicAuth as cba
from common import common as c

class repMan:
    def __init__(self,host,action,request_parameters):
        print("Replication Managment Called")
        self.request_parameters = request_parameters
        content_type,amz_date,payload_hash,authorization_header = cba.createSignture(cba(),host,action,self.request_parameters)
    
        self.headers = {'Content-Type':content_type,
        'X-Amz-Date':amz_date,
        'x-amz-content-sha256': payload_hash,
        'Authorization':authorization_header}


    def createReplication(self,endpoint):
        print("Create Replication Called")
        '''
        https://cloudbasic.net/documentation/api/CreateReplication/
        '''
        print('Request URL = ' + endpoint)
        r = requests.post(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()
    
    def finalizeReplication(self):
        print("Finalize Replication Called")
        '''
        https://cloudbasic.net/documentation/api/FinalizeReplication/
        '''
    
    def createAllReplication(self,endpoint):
        print("Create All Replication Called")
        '''
        https://cloudbasic.net/documentation/api/CreateAllReplication/
        '''
        print('Request URL = ' + endpoint)
        r = requests.post(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()

    def finalizeAllReplications(self):
        print("Finalize All Replication Called")
        '''
        https://cloudbasic.net/documentation/api/FinalizeAllReplications
        '''

    def getReplicationsList(self,endpoint):
        print("Get Replications List Called")
        '''
        https://cloudbasic.net/documentation/api/getreplicationslist
        '''
        print('Request URL = ' + endpoint)
        r = requests.post(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()


    def replicationStatus(self,endpoint):
        print("Replication Status Called")
        '''
        https://cloudbasic.net/documentation/api/ReplicationStatus
        '''
        print('Request URL = ' + endpoint)
        r = requests.post(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        return r.json()

    def alterReplication(self,endpoint):
        print("Alter Replication Called")
        '''
        https://cloudbasic.net/documentation/api/AlterReplication
        '''
        print('Request URL = ' + endpoint)
        r = requests.post(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            #This has to be done because there is NO response body
            return "Successfull Altered Replication Job"
    
    
    def deleteReplication(self):
        print("Delete Replication Called")
        '''
        https://cloudbasic.net/documentation/api/DeleteReplication
        '''

    def analyzeReplication(self,endpoint):
        print("Analyze Replication Called")
        '''
        https://cloudbasic.net/documentation/api/AnalyzeReplication
        '''

        print('Request URL = ' + endpoint)
        r = requests.post(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        if r.status_code not in [200]:
            print("Error Occurred on Return",r.text)
        else:
            return r.json()


    def createRedShiftReplication(self):
        '''
        https://cloudbasic.net/documentation/api/CreateRedshiftReplication
        '''
    def alterRedShiftReplication(self):
        '''
        https://cloudbasic.net/documentation/api/CreateRedshiftReplication
        '''
    
    def createS3Replication(self):
        print("Create S3 Replication Called")
        '''
        https://cloudbasic.net/documentation/api/CreateS3Replication
        '''

    def alterS3Replication(self):
        print("Alter S3 Replication Called")
        '''
        https://cloudbasic.net/documentation/api/AlterS3Replication
        '''
    
    def getLatency(self,endpoint):
        print("Get Latency Called")
        '''
        https://cloudbasic.net/documentation/api/getlatency/
        '''
        print('Request URL = ' + endpoint)
        r = requests.post(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        return r.json()

    def getLogs(self,endpoint):
        print("Get Logs Called")
        '''
        https://cloudbasic.net/documentation/api/getlogs/
        '''
        print('Request URL = ' + endpoint)
        r = requests.post(endpoint, data=self.request_parameters, headers=self.headers)
        print('Response code: ', r.status_code)

        return r.json()
    
    def rebuiltDbReplicaIndexes(self):
        print("Rebuild DB Replica Indexes Called")
        '''
        https://cloudbasic.net/documentation/api/rebuilddbreplicaindexes/
        '''

    def rebuiltDbReplicaIndexesStatus(self):
        print("Rebuild DB Replica Indexes Status Called")
        '''
        https://cloudbasic.net/documentation/api/rebuilddbreplicaindexesstatus/
        '''
    
    def reseedTable(self):
        print("Reseed Table Called")
        '''
        https://cloudbasic.net/documentation/api/reseedtable/
        '''
    
    def reseedTableStatus(self):
        print("Reseed Table Status Called")
        '''
        https://cloudbasic.net/documentation/api/reseedtablestatus/
        '''
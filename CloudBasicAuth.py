import sys, os, base64, datetime, hashlib, hmac,requests
from common import common as c
cfg = c.load_master_config()

class cloudBasicAuth:
    def __init__(self,method=None):
        print("Cloud Basic Auth Initialized")
        print("method: ",method)
        if not method:
            self.method = cfg['method']
        else:
            self.method = method
        
        self.service = cfg['service']
        self.region = cfg['region']
        self.content_type = cfg['content_type']
        self.access_key = cfg['access_key']
        self.secret_key = cfg['secret_key']

    def sign(self,key, msg):
        return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

    def getSignatureKey(self, date_stamp):
        kDate = self.sign(('AWS4' + self.secret_key).encode('utf-8'), date_stamp)
        kRegion = self.sign(kDate, self.region)
        kService = self.sign(kRegion, self.service)
        kSigning = self.sign(kService, 'aws4_request')
        return kSigning
    
    def createSignture(self,host,canonical_uri,request_parameters):
        t = datetime.datetime.utcnow()
        amz_date = t.strftime('%Y%m%dT%H%M%SZ')
        date_stamp = t.strftime('%Y%m%d') # Date w/o time, used in credential scope

        canonical_querystring = ''
        payload_hash = hashlib.sha256(request_parameters.encode('utf-8')).hexdigest()
        canonical_headers = 'content-type:' + self.content_type + '\n' + 'host:' + host + '\n' + 'x-amz-content-sha256:' + payload_hash + '\n' + 'x-amz-date:' + amz_date + '\n'

        signed_headers = 'content-type;host;x-amz-content-sha256;x-amz-date'

        canonical_request = self.method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

        algorithm = 'AWS4-HMAC-SHA256'
        credential_scope = date_stamp + '/' + self.region + '/' + self.service + '/' + 'aws4_request'
        string_to_sign = algorithm + '\n' +  amz_date + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

        signing_key = self.getSignatureKey(date_stamp)
        signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()
        authorization_header = algorithm + ' ' + 'Credential=' + self.access_key + '/' + credential_scope + ', ' +  'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

        return self.content_type,amz_date,payload_hash,authorization_header
# CloudBasic API

## **Incomplete other than the AWS Signature module --> WORK IN PROGRESS**

<https://cloudbasic.net/documentation/api/>

CloudBasic Library - Complete with all API endpoints using AWS Signature (v4) authentication

## AWS Signatures

<https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>

AWS Signatures can be a little hard to understand at first.  Every request that you send to the CloudBasic API has to be signed through the AWS Signature method (CloudBasicAuth)

There are several different ways to make a request, and each variant has to be handled disctinctively from the others.

CloudBasic API does not send anything in Query Parameters, but rather all in the body.

So we have to pass 'x-amz-content-sha256:' + payload_hash in the canonical_headers to account for that.

## Gotchas

Each METHOD ("GET" or "POST") has to be explicitly defined for the Signature and for the API request.  If a GET is used on the request (i.e. ReplicationServiceStatus), then GET also needs to be passed to the CloudBasicAuth module for signing.

CloudBasicAuth takes the METHOD from the Config file by default.

## Testing

Provided a test_script to run manual operations.  Also included common.py for loading the config and running Mongo queries, if any.

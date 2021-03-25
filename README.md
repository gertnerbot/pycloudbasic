# CloudBasic API

<https://cloudbasic.net/documentation/api/>

CloudBasic Library - Complete with all API endpoints using AWS Signature (v4) authentication

## AWS Signatures

<https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>

AWS Signatures can be a little hard to understand at first.  Every request that you send to the CloudBasic API has to be signed through the AWS Signature method (CloudBasicAuth)

There are several different ways to make a request, and each variant has to be handled disctinctively from the others.

CloudBasic API does not send anything in Query Parameters, but rather all in the body.

So we have to pass 'x-amz-content-sha256:' + payload_hash in the canonical_headers to account for that.

## Testing

Provided a test_script to run manual operations.  It will write a GetReplicationsList to disk for your viewing pleasure.

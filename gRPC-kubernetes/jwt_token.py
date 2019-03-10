import time, sys
import google.auth.crypt
import google.auth.jwt
import argparse
from argparse import RawTextHelpFormatter

def service_account(service, expiry_time=3600):
    iat = time.time()
    exp = iat+expiry_time
    if service == "ce":
        aud='endpoints-oa-ce.endpoints.wave16-joan.cloud.goog'
    elif service == "k8s":
        aud="grpc-k8s.endpoints.sbt-endpoints.cloud.goog"
    else:
        return "bad service env"

    payload={'iss': 'endpoints-sa@sbt-endpoints.iam.gserviceaccount.com',
             'sub': 'endpoints-sa@sbt-endpoints.iam.gserviceaccount.com',
             'aud': aud,
             'iat': iat,
             'exp': exp}
    
    signer = google.auth.crypt.RSASigner.from_service_account_file('key.json')
    jwt = google.auth.jwt.encode(signer, payload)
    return jwt.decode('utf-8')
    

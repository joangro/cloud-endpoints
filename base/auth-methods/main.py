import time, sys
import google.auth.crypt
import google.auth.jwt
import argparse
from argparse import RawTextHelpFormatter

def service_account(service, expiry_time=3600):
    iat = time.time()
    exp = iat+expiry_time
    if service == "ce":
        aud='endpoints-oa-ce.endpoints.sbt-endpoints.cloud.goog'
    elif service == "ae":
        aud="endpoints.sbt-endpoints.appspot.com"
    elif service == "k8s":
        aud="endpoints-oa-k8s.endpoints.sbt-endpoints.cloud.goog"
    else:
        sys.exit()
    payload={'iss': 'endpoints-sa@sbt-endpoints.iam.gserviceaccount.com',
             'sub': 'endpoints-sa@sbt-endpoints.iam.gserviceaccount.com',
             'aud': aud,
             'iat': iat,
             'exp': exp}
    
    signer = google.auth.crypt.RSASigner.from_service_account_file('key.json')
    jwt = google.auth.jwt.encode(signer, payload)
    print ("export JWT=" + jwt.decode("utf-8"))
    
    
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create JWT tokens for endpoints services', formatter_class=RawTextHelpFormatter)
    parser.add_argument('service', help="Create JWT for one of the services: \n \
                                        App Engine:\tae\n \
                                        Compute Engine:\tce\n \
                                        Kubernetes:\tk8s\n")
    args = parser.parse_args()
    service_account(args.service)

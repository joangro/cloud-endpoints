import time
import google.auth.crypt
import google.auth.jwt


def service_account(expiry_time=3600):
    iat = time.time()
    exp = iat+expiry_time

    payload={'iss': 'edit21@wave16-joan.iam.gserviceaccount.com',
             'sub': 'edit21@wave16-joan.iam.gserviceaccount.com',
             'aud': 'endpoints.wave16-joan.appspot.com',
             'iat': iat,
             'exp': exp}
    
    signer = google.auth.crypt.RSASigner.from_service_account_file('key.json')
    jwt = google.auth.jwt.encode(signer, payload)
    print (jwt.decode("utf-8"))
    
    
    
    
if __name__ == "__main__":
    service_account()

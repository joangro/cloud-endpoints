
## Before starting

1. Change `host:` in the `openapi.yaml` file:

```
host: "endpoints.<YOUR-PROJECT-ID>.appspot.com"
```

2. Add this same service name to your `app.yaml` file:

```
endpoints_api_service:
  name: endpoints.<YOUR-PROJECT-ID>.appspot.com
  rollout_strategy: managed
```

3. Change the service account of the `openapi.yaml` file:

    1. Create service account with a key file, see [this documentation](https://cloud.google.com/endpoints/docs/openapi/service-account-authentication#create_service_account). 
    
    2. Add the service account to the `openapi.yaml` file, in the following sections:
    
    ```
    securityDefinitions:
      service_account:
        authorizationUrl: ""
        flow: "implicit"
        type: "oauth2"
        x-google-issuer: "<ACCOUNT-NAME>@<YOUR-PROJECT-ID>.iam.gserviceaccount.com"
        x-google-jwks_uri: "https://www.googleapis.com/robot/v1/metadata/x509/<ACCOUNT-NAME>@<YOUR-PROJECT-ID>.iam.gserviceaccount.com"
    ```

## Deploying

1. Deploy service:

```
gcloud endpoints services deploy openapi.yaml
```

2. Deploy application:

```
gcloud app deploy
```


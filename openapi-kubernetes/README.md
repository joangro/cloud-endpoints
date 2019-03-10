## Before starting:

1. Change `host:` in the `openapi.yaml` file:

```
host: "endpoints-oa-k8s.endpoints.<YOUR-PROJECT-ID>.cloud.goog"
```

2. Change the service account of the `openapi.yaml` file:

    1. Create service account with a key file, see [this documentation](https://cloud.google.com/endpoints/docs/openapi/service-account-authentication#create_service_account). 
    
    2. Create an image of the application. See [this documentation](https://github.com/joangro/cloud-endpoints/tree/master/base/openapi-docker-application).
    
    3. Change the following in the `deployment.yaml` file:
      ```
      - name: esp
        image: gcr.io/endpoints-release/endpoints-runtime:1
        args: [
          "--http_port=8081",
          "--backend=0.0.0.0:8080",
          "--service=endpoints-oa-k8s.endpoints.<YOUR-PROJECT-ID>.cloud.goog",
          "--rollout_strategy=managed",
        ]
      ```
      
      ```
      - name: k8s-oa-api
        image: gcr.io/<YOUR-PROJECT-ID>/<YOUR-APPLICATION-IMAGE-ID>

      ```


    4. Add the service account to the `openapi.yaml` file, in the following sections:
    
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

2. Create Kubernetes cluster:

```
gcloud container clusters create YOUR-CLUSTER-NAME \
                                 --zone=YOUR-CLUSTER-ZONE \
                                 --machine-type=n1-standard-1 \
                                 --num-nodes=1 \
                                 --scopes=cloud-platform,datastore
```

3. Get cluster credentials:

```
gcloud container clusters get-credentials YOUR-CLUSTER-NAME --zone=YOUR-CLUSTER-ZONE
```

4. Deploy Kubernetes deployment:
```
kubectl create -f deployment.yaml
```

5. Get external cluster IP, used for calling the API:
```
kubectl get service
```

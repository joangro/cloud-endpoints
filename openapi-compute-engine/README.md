## Before starting:

1. Change `host:` in the `openapi.yaml` file:

```
host: "endpoints-oa-ce.endpoints.<YOUR-PROJECT-ID>.cloud.goog"
```

2. Change the service account of the `openapi.yaml` file:

    1. Create service account with a key file, see [this documentation](https://cloud.google.com/endpoints/docs/openapi/service-account-authentication#create_service_account). 
    
    2. Create an image of the application. See [this documentation](https://github.com/joangro/cloud-endpoints/tree/master/base/openapi-docker-application).

## Building Compute Engine OpenAPIenvironment:

1. Deploy Endpoints service:

```
gcloud endpoints services deploy openapi.yaml
```

2. Create Compute Engine Instance with docker:

```
gcloud compute instances create openapi \
	--image-family debian-9 \
	--image-project debian-cloud \
	--machine-type n1-standard-1 \
	--scopes=cloud-platform,datastore \
	--zone europe-west1-c \
	--tags=http-server,https-server \
	--metadata-from-file startup-script=startup-script.sh
```

3. Connect to instance:

```
gcloud compute ssh openapi --zone europe-west1-c
```

## Deploying:

0. Authenticate Docker:

```
gcloud auth configure-docker
``` 

1. Pull image locally:

```
sudo gcloud docker -- pull gcr.io/sbt-endpoints/endpoints-image:v0
```

2. Create docker service
    
```
sudo docker network create --driver bridge esp_net
```

3. Create application container

```
sudo docker run  --detach \
                 --name=endpoints-oa-ce \
                 --net=esp_net gcr.io/sbt-endpoints/endpoints-image:v0
```

3. Create ESP proxy container pointing to application

```
sudo docker run --name=esp \
		--detach \
		-p 80:8080 \
		--net=esp_net \
		gcr.io/endpoints-release/endpoints-runtime:1 \
		--service=endpoints-oa-ce.endpoints.sbt-endpoints.cloud.goog \
		--rollout_strategy=managed \
		--backend=endpoints-oa-ce:8080
```

4. Expose CE instance to receive traffic:

```
gcloud compute firewall-rules create p80 --allow tcp:80
```


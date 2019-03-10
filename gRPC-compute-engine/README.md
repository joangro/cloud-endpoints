## Before starting:

1. Change the "name" field in the api_config.yaml file:
```
name: grpc-ce.endpoints.<YOUR-PROJECT-ID>.cloud.goog
```

2. Change the image and service in the deployment.yaml file.

2. Create grpc libraries and api_descriptor.pb file:
```
python  -m grpc_tools.protoc \
        --include_imports \
        --include_source_info \
        --proto_path=./protos \
        --descriptor_set_out=api_descriptor.pb \
        --python_out=. \
        --grpc_python_out=. \
        ./protos/endpoints.proto
```

3. Deploy service:
```
gcloud endpoints services deploy api_descriptor.pb api_config.yaml
```

## Setting up environment and deploying:

1. Create Compute Engine VM:

```
gcloud compute instances create grpc \
	--image-family debian-9 \
	--image-project debian-cloud \
	--machine-type n1-standard-1 \
	--scopes=cloud-platform,datastore \
	--zone europe-west1-c \
	--tags=http-server,https-server \
	--metadata-from-file startup-script=startup-script.sh
```

2. Create docker network

```
sudo docker network create --driver bridge esp_net
```

3. Download API container locally:
```
sudo gcloud docker -- pull gcr.io/sbt-endpoints/grpc-endpoints:v1
```

4. Deploy API container:
```

sudo docker run \
    --detach \
    --name=grpc-ce \
    --net=esp_net \
    gcr.io/sbt-endpoints/grpc-endpoints:v1
```

5. Deploy ESP container:
```
sudo docker run \
    --detach \
    --name=esp \
    --publish=80:9000 \
    --net=esp_net \
    gcr.io/endpoints-release/endpoints-runtime:1 \
    --service=grpc-ce.endpoints.<YOUR-PROJECT-ID>.cloud.goog \
    --rollout_strategy=managed \
    --http2_port=9000 \
    --backend=grpc://grpc-ce:8080
```


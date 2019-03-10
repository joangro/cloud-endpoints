## Before starting:

1. Change the "name" field in the api_config.yaml file:
```
name: grpc-k8s.endpoints.<YOUR-PROJECT-ID>.cloud.goog
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

4. Create Kubernetes Cluster:
```
gcloud container clusters create <YOUR-CLUSTER-NAME> \
                                 --zone=<YOUR-CLUSTER-ZONE> \
                                 --machine-type=n1-standard-1 \
                                 --num-nodes=1 \
                                 --scopes=cloud-platform,datastore
```

## Deploying:

1. Get Kubernetes cluster credentials:
```
gcloud container clusters get-credentials <YOUR-CLUSTER-NAME>  --zone <YOUR-CLUSTER-ZONE> --project <YOUR-PROJECT-ID>
```

2. Deploy image to cluster:
```
kubectl create -f deployment.yaml
```

3. Get kubernetes cluster external IP:
```
kubectl get service
```

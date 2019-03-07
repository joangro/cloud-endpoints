Generate descriptor file:

python -m grpc_tools.protoc \
    --include_imports \
    --include_source_info \
    --proto_path=./protos \
    --descriptor_set_out=api_descriptor.pb \
    --python_out=. \
    --grpc_python_out=. \
    ./protos/endpoints.proto

Deploy image to cluster:

kubectl -f apply 

Get kubernetes cluster external IP:

kubectl get service

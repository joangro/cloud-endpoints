    sudo docker run --detach --name=endpoints-oa-ce --net=esp_net gcr.io/wave16-joan/endpoints-image:v0



    sudo docker run     --name=esp \
                        --detach \
                        --publish=8080:8080 \
                        --net=esp_net \
                        gcr.io/endpoints-release/endpoints-runtime:1 \
                        --service=endpoints-oa-ce.endpoints.wave16-joan.cloud.goog \
                        --rollout_strategy=managed \
                        --backend=endpoints-oa-ce:8080 


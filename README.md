# Google Cloud Endpoints #

![Endpoints logo](https://3.imimg.com/data3/FE/PW/MY-12444595/qq-500x500.jpg)

Example implementations of the [Google Cloud Endpoints](https://cloud.google.com/endpoints/) API Managment service. 
Cloud Endpoints offers the possibility to implement and API service with three communications protocols: OpenAPI, gRPC and Endpoints Frameworks.

This repository implements all of the environments where the Cloud Endpoints APIs can run, except for pure Kubernetes environments, as these were done already in GKE.

Status of the Cloud Endpoints runtimes at the state of the creation of this repository (March 2019):


|     Environment      |      OpenAPI       |         gRPC          | Endpoints Frameworks |
| ---------------------|:------------------:|:---------------------:|:--------------------:|
|  Kubernetes          | :heavy_check_mark: |   :heavy_check_mark:  |  :x:                 |
|  Compute Engine      | :heavy_check_mark: |   :heavy_check_mark:  |  :x:                 |
|  App Engine Flex     | :heavy_check_mark: |   :x:                 |  :x:                 |
|  App Engine Standard | :x:                |   :x:                 |  :heavy_check_mark:  |


## API baseline structure ##

All the APIs, despite running in different environments/frameworks, are designed with the same baseline logic:

1. All APIs are written in Python
2. All APIs communicate to [Datastore](https://cloud.google.com/datastore/docs/concepts/overview) in the backend, to perform the API logic/operations. All the environments use the [Datastore Cloud Client Libraries](https://googleapis.github.io/google-cloud-python/latest/datastore/client.html), except for Endpoints Frameworks, which uses the [Python NDB Client Library](https://cloud.google.com/appengine/docs/standard/python/ndb/).

### API structure overview ###

The APIs have the following method/handler:

###### GET /users ######

- Request parameters: *None*
- Authentication required: **API Key**
- Limits: *None*
- Response: List of users

###### GET /users/{user} ######

- Request parameters:
    - **user**: Required - in path
    - **age**: Optional - in body
- Authentication required: **API Key**
- Limits: **5 requests/min**
- Response: User entity properties

###### PUT /users/{user} ######

- Request parameters:
    - **user**: Required - in path
    - **age**: Optional - in body
- Authentication required (**both are required!**): 
    - **API Key**
    - **JWT Token**
- Limits: *None*
- Response: Status (OK/ERROR)

###### DELETE /users/{user} ######

- Request parameters:
    - **user**: Required - in path
- Authentication required: **API Key**
- Limits: *None*
- Response: Status (OK/ERROR)

## Repository Structure ##

* **base**: The base code for the three API implementations. It includes the following:

    * [openapi-flask-application](/base/openapi-flask-application): The base API code for OpenAPI implementations. Based in [Flask](http://flask.pocoo.org/) and  [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/).
    
    * [openapi-docker-application](/base/openapi-docker-application): The same previous API code, but with an additional script to Dockerize it.
    
    * [grpc-application](/base/grpc-application): Base code for gRPC based APIs.
    
    * [endpoints-frameworks](/base/endpoints-frameworks): Base code for the Endpoints Frameworks implementation.
    
    * [auth-methods](/base/auth-methods): Code to create the credentials/tokens in order to authenticate into some of the API handlers.

* **endpoints-frameworks**: Implementation of the [Endpoints Frameworks](https://cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks) App Engine framework, in App Engine Standard using the Python runtime.

* **gRPC-compute-engine**: Implementation of the [gRPC framework](https://cloud.google.com/endpoints/docs/grpc/about-grpc) API in [Compute Engine](https://cloud.google.com/endpoints/docs/grpc/get-started-compute-engine-docker).

* **gRPC-kubernetes**: Implementation of the [gRPC framework](https://cloud.google.com/endpoints/docs/grpc/about-grpc) API in [ Google Kubernetes Engine (GKE)](https://cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine).

* **openapi-app-engine-flexible**: Implementation of the [OpenAPI management system](https://cloud.google.com/endpoints/docs/openapi/) in [App Engine Flexible](https://cloud.google.com/endpoints/docs/openapi/get-started-app-engine), the Python runtime.

* **openapi-compute-engine**: Implementation of the [OpenAPI management system](https://cloud.google.com/endpoints/docs/openapi/) in [Compute Engine](https://cloud.google.com/endpoints/docs/openapi/get-started-compute-engine-docker).

* **openapi-kubernetes**:  Implementation of the [OpenAPI management system](https://cloud.google.com/endpoints/docs/openapi/) in [Google Kubernetes Engine (GKE)](https://cloud.google.com/endpoints/docs/openapi/get-started-kubernetes-engine).




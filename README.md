# Google Cloud Endpoints #

Example implementations of the [Google Cloud Endpoints](https://cloud.google.com/endpoints/) API Managment service. 
Cloud Endpoints offers the possibility to implement and API service with three communications protocols: OpenAPI, gRPC and Endpoints Frameworks.

## Repository Structure ##

* **Base**: The base code for the three API implementations. It includes the following:

    * **openapi-flask-application**: The base API code for OpenAPI implementations. Based in [Flask](http://flask.pocoo.org/) and  [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/).
    
    * **openapi-docker-application**: The same previous API code, but with an additional script to Dockerize it.
    
    * **grpc-application**: Base code for gRPC based APIs.
    
    * **endpoints-frameworks**: Base code for the Endpoits Frameworks implementation.
    
    * **auth-methods**: Code to create the credentials/tokens in order to authenticate into some of the API handlers.

Build openAPI file:

```
python lib/endpoints/endpointscfg.py get_openapi_spec main.UsersAPI --hostname  endpoints-frameworks.wave16-joan.appspot.com
```

Deploy service:

```
gcloud endpoints services deploy usersv1openapi.json
```

Test locally with:

```
dev_appserver.py ./app.yaml
```

*Note*: This won't work, because there is no local datastore emulator configured, and the ndb library can't connect to the Datastore Client from a local environment

Deploy:

```
gcloud app deploy --version last
```

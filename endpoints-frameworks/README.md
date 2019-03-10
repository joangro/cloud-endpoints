1. Build openAPI file:

```
python lib/endpoints/endpointscfg.py get_openapi_spec main.UsersAPI --hostname  endpoints-frameworks.wave16-joan.appspot.com
```

2. Deploy service:

```
gcloud endpoints services deploy usersv1openapi.json
```

3. Test locally with:

```
dev_appserver.py ./app.yaml
```

*Note*: This won't work at all, because there is no local datastore emulator configured, and the ndb library can't connect to the Datastore Client from a local environment.


4. Deploy:

```
gcloud app deploy --version last
```


5. Test:

curl <...>/_ah/api/users/v1/users

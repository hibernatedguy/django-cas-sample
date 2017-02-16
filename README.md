# django-cas-sample
Client and Server example for Centralised Authentication Server.
Sample database is already present with cas-client and cas-server
# Setup
### install requirements file
```pip install requirements.txt```

### make client-app running
```
cd cas_client/
python manage.py migrate
python manager.py runserver 8080
```

### make cas-server app running
```
cd cas_server/
python manage.py migrate
python manager.py runserver 9090
```
#### Sample accounts for cas-server
```
username : sunit
password : 7uiop098

username : ashish
password : 7uiop098
```

# steps to test client and server app
go to http://localhost:8080

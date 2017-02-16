# djang-cas-sample
Client and Server example for Centralised Authentication Server.

# install requirements file
pip install requirements.txt

# make client-app running
cd cas_client
python manage.py migrate
python manager.py runserver 8080

# make cas-server app running
cd cas_server
python manage.py migrate
python manager.py runserver 9090

# steps to test client and server app
go to http://localhost:8080



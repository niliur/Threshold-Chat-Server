# Threshold-Chat-Server

To set up:
1. cd to the threshold-chat directory
2. if you've made changes to the models, first run:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
3. then, start the server with:
```
$ python3 manage.py runserver
```
4. open localhost:8000/tcserver in a browser to see the UI

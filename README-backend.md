# vue_djacket

## Install libraries
```
pip install -r required.txt
```

### Setup server
```
python django_jacket/manage.py makemigrations
python django_jacket/manage.py migrate
```

### Create admin account
```
python django_jacket/manage.py createsuperuser
```

### Run server
```
python django_jacket/manage.py runserver
```

### add stuff product to backend
```
http://localhost:8000/admin/
```
I suggest to add category winter and summer with slug winter and summer as well, otherwise case page will not work properly.
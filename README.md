# django-todoApp
my first django app


## kurulumlar

### Python3

``sudo apt-get install gcc``

``sudo apt-get install python3 python3-pip python3-dev libpq-dev``


### PostgreSQL

``sudp apt-get install libpq-dev postgresql postgresql-contrib``

```
sudo su - postgres

psql

CREATE DATABASE todoApp;

CREATE USER appuser WITH PASSWORD 'toor';

ALTER ROLE appuser SET client_encoding TO 'utf8';
ALTER ROLE appuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE appuser SET timezone TO 'UTC+3';


GRANT ALL PRIVILEGES ON DATABASE todoApp TO appuser;

\q

exit
```

``sudo pip3 install virtualenv``

``virtualenv todoAppenv``

``source todoAppenv/bin/activate``

### django

``sudo pip3 install django``

``sudo apt-get install python3-psycopg2``

``django-admin startproject djangotodoApp .``
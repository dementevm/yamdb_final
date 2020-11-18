![Yamdb_final_workflow](https://github.com/dementevm/yamdb_final/workflows/Yamdb_final_workflow/badge.svg)

## api_yamdb
API part for YamDB project, that allows to get data of users, titles, rewievs and comments.
## Prerequisites
Download and Install [Docker](https://www.docker.com/).
```
sudo apt update
```
```
sudo sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
```
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 
```
```
sudo apt update 
```
```
sudo apt install docker-ce -y 
```
Download and install [Docker-compose](https://docs.docker.com/compose/install/)
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```
sudo chmod +x /usr/local/bin/docker-compose
```
## Deployment
1. Download repository via github, or clone repository ```git clone https://github.com/dementevm/api_yamdb```
2. Navigate to project folder.
3. Create .env file with following settings: 
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_database_name
POSTGRES_USER=your_database_user
POSTGRES_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432
```
4. Execute command ```docker-compose up```
5. For making migrations get project container id - ```docker container ls```.
Run command ```docker exec -it <CONTAINER ID> python manage.py migrate```

Project will be available locally at http://0.0.0.0:8000

### Django commands
To use django commands via terminal from container follow next steps:
1. Get project container id - ```docker container ls```
2. Enter container terminal - ``` docker exec -it <CONTAINER ID> bash```

Create superuser command - ```python manage.py createsuperuser```

To fill database with test data - ``` python manage.py loaddata fixtures.json```

To exit container terminal type ```exit```

### Built With
[Django](https://www.djangoproject.com/) - web framework.

[Django REST Framework](https://www.django-rest-framework.org/) - toolkit for building Web APIs.

[Gunicorn](https://gunicorn.org/) - a Python WSGI HTTP Server for UNIX.

[Docker](https://www.docker.com/) - an open platform for developing, shipping, and running applications.

[PostgreSQL](https://www.postgresql.org/) - open source relational database

[Python](https://www.python.org/) - 🐍

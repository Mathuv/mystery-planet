# Mystery Planet

Life on Mystery Planet. Check out the project's [documentation](http://mathuv.github.io/mystery-planet/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

## With Docker

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

### Local documentation access

Main documentation site:

- [http://localhost:8001/](http://localhost:8001/)

Documentation of APIs related to people/persons

- [http://localhost:8001/api/persons/](http://localhost:8001/api/persons/)

## Without docker

Create python virtual environment and activate it.

```bash
 python -m venv .venv && source .venv/bin/activate && pip install --upgrade pip setuptools
```

Install the required python packages

```bash
 pip install -r requirements.txt
```

Make sure you have a running PostgreSQL instance and a brand new database (for the first time)

Set the environment variables. Check the `.env.sample` file in the repo.

```bash
DJANGO_SECRET_KEY=<secret_key>
DATABASE_URL=postgres://<postgres_user>:<postgres_password>@<postgres_host>:5432/<postgres_db>
```

To apply the migrations to the databse:

```bash
python manage.py migrate
```

To run the API Server locally (in development mode):

```bash
python manage.py runserver
```

To run all the unit tests:
```bash
pytest mystery-planet
```



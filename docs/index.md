# Mystery Planet

Life on Mystery Planet. Check out the project's [documentation](http://mathuv.github.io/mystery-planet/).

# 1. Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# 2. Local Development

## 2.1. With Docker

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

### 2.1.1. Local documentation access

Main documentation site:

- [http://localhost:8001/](http://localhost:8001/)

Documentation of APIs related to people/persons

- [http://localhost:8001/api/persons/](http://localhost:8001/api/persons/)

## 2.2. Without docker

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
pytest mystery_planet
```

### 2.2.1. Loading the data (ETL)

Json files containing the data for companies, people and foods are found under the `resources` folder. 

```
companies.json - Company data
people.json - people/persons data
food.json - food (master) data
```

There are thee Django Management Commands to _**transform**_ and _**load**_ data into the database from each file.

- Load company data (resources/companies.json)

```bash
 ./manage.py load_company_data
```

By default, the command uses the file resources/companies.json while a custom file can be provided with the command option '--data-file'


```bash
 ./manage.py load_company_data --data-file <DATA_FILE>
```

- Load food master data (resources/food.json)

The file food.json is created to hold the data of different food items and their type (such as fruits, vegetables etc) which are found under people.json.

```bash
 ./manage.py load_food_data
```

By default, the command uses the file resources/food.json while a custom file can be provided with the command option '--data-file'


```bash
 ./manage.py load_food_data --data-file <DATA_FILE>
```

- Load people data (resources/people.json)

```bash
 ./manage.py load_person_data
```

By default, the command uses the file resources/people.json while a custom file can be provided with the command option '--data-file'


```bash
 ./manage.py load_person_data --data-file <DATA_FILE>
```

# 3. TODO

```markdown
## Todo

- [ ] Add more docstrings and inline comments
- [ ] Improve the performance of the management command 'load_person_data'
- [ ] Add logging
- [ ] Handle exceptional conditions

## In Progress

- [ ] Write more unit tests and integration tests

## Done
```


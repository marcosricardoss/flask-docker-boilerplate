# Flask Docker Boilerplate

Use this doilerplate application to quickly setup and start to create a Flask HTTP REST API.


## Features

- SQLAlchemy ORM
- Flask-Migrate
- Pytest
- Line Commands
- Twelve-factor methodology
- SOLID design principles
- PEP-8 for code style
- Heroku deployable
- JWT authentication
- Docker

## Strategy

This Flask boilerplate uses the **MVC** as its base architecture, where the *blueprint* package is the controller layer and the *model* package is the model layer.

The interface with the model layer is given by classes that use the **Repository Pattern**, containing the business rules of the application. Associated with the **Strategy Pattern**, it not only provides a user-friendly interface with the model layer but also implements the **SOLID** principles **Single Responsibility Principle** and **Open / Closed Principle**, which avoids tight couplings.


## Configuring and Running The Application

The following steps are required to run the application


### Configure The Database

This Flask boilerplate support to work with PostgreSQL and SQLite databases. With the database configured, you need to make the database URI containing the database credentials to access it. This URI will be set later for application through environment variables.

Database URIs examples:

	PostgreSQL: postgresql+psycopg2://username:123@127.0.0.1:15432/database_name
	SQLite: sqlite:////usr/src/flaskapp/data/database.db


### Running 

In a Linux or Unix-like SO, you can use the bash script of the 'bin' directory to set the the environment variables and run the docker container in one-time.

`bash bin/prod up`<br>
`bash bin/prod up --build`<br>

Or if you prefer you set the environment variables manually and run the docker container after.

The FLASK_ENV is a Flask environment variable using to configure the flask execution. In the project this variable is set trough the ENV enviroment varible in the docker-compose.yml, therefore you must to use the same values accept by the FLASK_ENV to the ENV in the bash scripts.


### Performing Database Migration

If you need do a databata migration, use de comand bellow to run it in the running container:

`docker exec -it flask-docker-boilerplate flask db upgrade`<br>


**Tests**

After run the application configured to a testing environment using the `bash bin/test up` command, run the commands below to run the tests: 

Running with pytest:

`docker exec -it flask-docker-boilerplate pytest`

Running with coverage:

`docker exec -it flask-docker-boilerplate coverage run -m pytest`


## Examples of Use

You can use the Postman to try the HTTP REST API. Download 
*Postman Collections* of requests in the link below and import to Postman. 

[Download Postman Collections](https://www.getpostman.com/collections/f177968870d56e2828a3 "Download Postman Collections")

This Postman collection was made based on:

	Host: 127.0.0.1
	Port: 5000

**Note: To access a protected view, all we have to do is send in the JWT with the request. By default, this is done with an authorization header that looks like::**

	Authorization: Bearer <access_token>

	
## Contributing

Whether reporting bugs, discussing improvements and new ideas or writing extensions: Contributions are welcome! Here's how to get started:

1. Fork the repository on Github, create a new branch off the master branch and start making your changes (known as[ GitHub Flow](https://guides.github.com/introduction/flow/index.html " GitHub Flow"))
2. Write a test which shows that the bug was fixed or that the feature works as expected
3. Send a pull request and bug the maintainer until it gets merged and published
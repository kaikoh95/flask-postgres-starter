# Flask Postgres Starter

## Intro
Starter template for Python Flask, PostgreSQL, Flask Caching (RedisCache), and Dockerfile.

Contains a simple REST API service example that was written in a self-documenting format
such that Swagger docs can be generated automatically via the example schemas and decorators.

This uses PostgreSQL for persistence and Flask Caching (RedisCache) for caching results.

## Usage
Ensure that you have [Docker](https://www.docker.com/) installed in your host machine before trying to run the application.

```
$ git clone https://github.com/kaikoh95/flask-postgres-starter.git
$ cd flask-postgres-starter
$ docker-compose up --build
```
Now redirect to http://localhost:5000.

Once you have your local server running,
you can test your server using Postman and
view Swagger docs [here](http://localhost:5000/swagger-ui).


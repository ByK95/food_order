<div id="top"></div>

[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Food Order</h3>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This a playground project for async web architecture. Where services might be divided into multiple microservices general principles are simple.

Request -> 
    Endpoint Handles the request and returns a promise -> 
    At this point response is generated and send to user ->
    generated promise is actually a task id thats queued into rabbitmq for complex calculations ->
    after complex calculations handled asynchronously the result is saved to rabbitmq ->
    given any time user can query and ask for promise status 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Docker](https://www.docker.com/)
* [Python](https://vuejs.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [RabbitMQ](https://www.rabbitmq.com/)
* [PostgreSql](https://www.postgresql.org/)
* [Sqlalchemy](https://www.sqlalchemy.org/)
* [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
* [flasgger](https://github.com/flasgger/flasgger)
* [marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* [black](https://github.com/psf/black)



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* [docker](https://docs.docker.com/get-docker/)
* [docker-compose](https://docs.docker.com/compose/)
  

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   cd Project-Name
   ```
2. Run to get it started.
   ```sh
   docker-compose build
   docker-compose up -d
   ```
3. Prepare db migrations
   ```sh
   docker-compose exec web flask db init
   docker-compose exec web flask db upgrade
   ```
4. populate db with some data
   ```sh
   docker-compose exec web python seed.py
   ```
5. now you should be able to test

### Extra:
for shell access use:
 ```sh
   docker-compose exec web flask shell
   ```
after model changes use:
 ```sh
   docker-compose exec web flask db migrate -m "migration commit message"
   ```

### Testing:
```sh
docker-compose exec web python -m unittest
```

<p align="right">(<a href="#top">back to top</a>)</p>


### Docs

[Swagger Documentation](http://localhost:8080/apidocs/)

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



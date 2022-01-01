docker-compose exec web flask db init
docker-compose exec web flask db migrate -m "Init migration"
docker-compose exec web flask db upgrade

docker-compose exec web flask shell

docker-compose exec web black shell.py

docker exec -it ccf081351bfb bash

docker-compose exec web python -m unittest
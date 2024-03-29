ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY: down help jupyter jupyter-with-mysql main test up

help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "down               – Stop local MySQL server"
	@echo "help               – Show this help"
	@echo "jupyter            – Start jupyter notebook"
	@echo "jupyter-with-mysql – Start jupyter notebook with local MySQL server"
	@echo "mysql              – Start shell to local MySQL server"
	@echo "test               – Run all unit and integration tests"
	@echo "up                 – Start local MySQL server"

down:
	docker-compose down

jupyter-with-mysql:
	make up
	make jupyter
	make down

jupyter:
	PYTHONPATH="$(ROOT_DIR)" jupyter notebook --notebook-dir=notebooks

mysql:
	docker-compose exec mysql mysql --user=root --password=secret serlo

test:
	pytest

up:
	./start_mysql.sh

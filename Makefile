ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY: down help jupyter test up

down:
	docker-compose down

help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "down    – Stop local mysql server"
	@echo "help    – Show this help"
	@echo "jupyter – Start jupyter notebook"
	@echo "test    – Run all unit and integration tests"
	@echo "up      – Start local mysql server"

jupyter:
	PYTHONPATH="$(ROOT_DIR)" jupyter notebook --notebook-dir=notebooks

test:
	pytest

up:
	docker-compose up --detach

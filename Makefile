ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY: help jupyter test up down

help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "jupyter – Start jupyter notebook"
	@echo "help    – Show this help"
	@echo "test    – Run all unit and integration tests"
	@echo "up      – Start local mysql server"
	@echo "down    – Stop local mysql server"

jupyter:
	PYTHONPATH="$(ROOT_DIR)" jupyter notebook --notebook-dir=notebooks

test:
	pytest

up:
	docker-compose up --detach

down:
	docker-compose down

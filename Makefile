.PHONY: help

help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "jupyter – Start jupyter notebook"
	@echo "help    – Show this help"
	@echo "test    – Run all unit and integration tests"

jupyter:
	jupyter notebook --notebook-dir=notebooks

test:
	pytest

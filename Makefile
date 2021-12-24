.PHONY: help

help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "jupyter – Start jupyter notebook"
	@echo "help    – Show this help"

jupyter:
	jupyter notebook --notebook-dir=src

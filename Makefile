#!/bin/bash
.PHONY: test run synthax

venv:
	( \
		python -m pip install --upgrade pip; \
		pip install virtualenv; \
		python -m venv venv; \
		source venv/Scripts/activate; \
		pip install -r requirements.txt; \
	)

## CI Scripts
synthax: venv
	( \
		source venv/Scripts/activate; \
		pip install flake8; \
		echo "flake8 analyze :"; \
		flake8 src --count --exit-zero --max-complexity=10 --max-line-length=120 --show-source --statistics; \
		echo "flake8 ended."; \
	)

test: venv
	( \
		source venv/Scripts/activate; \
		pip install coverage; \
		python -m coverage run -m unittest; \
		coverage report -m; \
	)

## Run script
run: venv
	( \
		source venv/Scripts/activate; \
		python main.py; \
	)

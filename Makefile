#!/bin/bash
.PHONY: test run

venv:
	( \
		python3.10 -m pip install --upgrade pip; \
		pip install virtualenv; \
		python3.10 -m venv venv; \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
	)

## CI Scripts
synthax: venv
	( \
		source venv/bin/activate; \
		pip install flake8; \
		echo "flake8 analyze :"; \
		flake8 src --count --exit-zero --max-complexity=10 --max-line-length=120 --show-source --statistics; \
		echo "flake8 ended."; \
	)

test: venv run
	( \
		source venv/bin/activate; \
		pip3.10 install coverage; \
		python3.10 -m coverage run -m unittest; \
		coverage report -m; \
	)

## Run script
run: venv
	( \
		source venv/bin/activate; \
		python3.10 main.py; \
	)

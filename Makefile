.PHONY: version clean test tox reformat lint docs build publish

clean:
	rm -rf build dist *.egg-info

test:
	coverage run manage.py test
	coverage report

tox:
	rm -rf .tox
	tox

reformat:
	isort -rc src/django_icons
	isort -rc tests
	isort -rc *.py
	autoflake -ir *.py src/django_icons tests --remove-all-unused-imports
	docformatter -ir --pre-summary-newline --wrap-summaries=0 --wrap-descriptions=0 src/django_icons tests *.py
	black .

lint:
	flake8 bootstrap3 src tests *.py
	pydocstyle --add-ignore=D1,D202,D301,D413 src tests *.py

docs:
	cd docs && sphinx-build -b html -d _build/doctrees . _build/html

build: clean docs
	python setup.py sdist bdist_wheel
	twine check dist/*

publish: build
	twine upload dist/*

.PHONY: clean test tox reformat publish docs build publish

clean:
	rm -rf build dist *.egg-info

test:
	coverage run manage.py test && coverage report

tox:
	rm -rf .tox
	tox

reformat:
	isort -rc django_icons
	isort -rc tests
	autoflake -ir django_icons tests --remove-all-unused-imports
	black .
	flake8 django_icons tests

docs:
	cd docs && sphinx-build -b html -d _build/doctrees . _build/html

build: clean docs
	python setup.py sdist bdist_wheel
	twine check dist/*

publish: build
	twine upload dist/*

.PHONY: clean test tox reformat publish

clean:
	rm -rf build dist *.egg-info

test:
	python manage.py test

tox:
	rm -rf .tox
	tox

reformat:
	isort -rc django_icons
	isort -rc tests
	autoflake -ir django_icons tests --remove-all-unused-imports
	black .
	flake8 django_icons tests

publish: clean
	cd docs && make html
	python setup.py sdist bdist_wheel upload

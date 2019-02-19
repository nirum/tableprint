all:
	python setup.py install

develop:
	python setup.py develop

upload:
	python setup.py sdist bdist_wheel
	twine upload dist/*

test2:
	python2 -m nose --logging-level=INFO

test:
	nosetests -v --with-coverage --cover-package=tableprint --logging-level=INFO

clean:
	rm -R tableprint.egg-info
	rm -f tableprint/*.pyc
	rm -R tableprint/__pycache__/

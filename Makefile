all:
	python setup.py install

develop:
	python setup.py develop

upload:
	python setup.py sdist bdist_wininst upload

test2:
	python2 /usr/local/bin/nosetests --logging-level=INFO

test:
	nosetests -v --with-coverage --cover-package=tableprint --logging-level=INFO

clean:
	rm -rf tableprint.egg-info
	rm -f *.pyc
	rm -rf __pycache__

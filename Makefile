all:
	python setup.py install

develop:
	python setup.py develop

upload:
	python setup.py sdist upload

test2:
	python2 /Users/nirum/anaconda/bin/nosetests --logging-level=INFO

test:
	nosetests -v --with-coverage --cover-package=tableprint --logging-level=INFO

clean:
	rm -R tableprint.egg-info
	rm -f tableprint/*.pyc
	rm -R tableprint/__pycache__/

all:
	python setup.py install

develop:
	python setup.py develop

upload:
	python setup.py sdist bdist_wininst upload

clean:
	rm -rf tableprint.egg-info
	rm -f *.pyc
	rm -rf __pycache__

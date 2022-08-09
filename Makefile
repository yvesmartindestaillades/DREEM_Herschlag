DOCKER_IMAGE := ydmt/DREEM_Herschlag
VERSION := $(shell git describe --always --dirty --long)
default:
	echo "See readme"
	pip3 uninstall DREEM_Herschlag -y
	pip3 install .
	
init:
	pip install -r requirements.txt

pin-dependencies:
	pip install -U pip-tools
	pip-compile requirements.in

upgrade-dependencies:
	pip install -U pip pip-tools
	pip-compile -U requirements.in > requirements.txt

push_to_pypi:
	pip3 uninstall DREEM_Herschlag -y
	pip3 install .
	rm -fr dist
	python3 -m build
	twine upload -r pypi dist/*

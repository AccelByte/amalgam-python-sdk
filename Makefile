PYPI_URL=https://test.pypi.org/legacy/

all:
	@echo Targets
	@echo
	@echo "push        - push justice iam python sdk to pypi"
	@echo "clean        - push justice iam python sdk to pypi"
	@echo

clean:
	rm -rf dist/
	rm -rf justice_iam_python_sdk.egg-info

push:
	python setup.py sdist
	twine upload --repository-url $(PYPI_URL) dist/*
	rm -rf dist/
	rm -rf justice_iam_python_sdk.egg-info

CONDA_ENV ?= ledgerx

test:
	@pytest -s .

release:
	@python setup.py sdist
	@twine upload dist/*

env.create:
	@conda create -y -n ${CONDA_ENV} python=3.7

env.update:
	@conda env update -n ${CONDA_ENV} -f environment.yml


from setuptools import setup, find_packages


setup(
    name = "package",
    version = "0.1",
    packages = find_packages(exclude=['*test']) # , cosa vuol dire di preciso?
	)
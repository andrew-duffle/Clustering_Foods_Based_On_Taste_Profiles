from setuptools import setup, find_packages

setup(
	name='Project2',
	version='1.0',
	author='Andrew Duffle',
	author_email='andrew.g.duffle-1@ou.edu',
	packages=find_packages(exclude=('tests','docs'))
)

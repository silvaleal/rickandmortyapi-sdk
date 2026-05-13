from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='UORickandmortyapi_sdk',
    version='0.0.1',
    license='MIT License',
    author='silvaleal',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='me@silvaleal.dev',
    keywords='sdk api rickandmorty rick morty',
    description=u'SDK da api rickandmorty não oficial',
    packages=[],
    install_requires=['requests'],)
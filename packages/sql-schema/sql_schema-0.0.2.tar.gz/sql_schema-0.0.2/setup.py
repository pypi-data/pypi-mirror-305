from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'Schema Transfer/Drop Helper'
LONG_DESCRIPTION = 'A package that allows to transfer or drop a schema without any hassle.'

# Setting up
setup(
    name="sql_schema",
    version=VERSION,
    author="Mohammed Abu Bakkar Kuchikar",
    author_email="abu813684@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/plain",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pypyodbc'],
    keywords=['python', 'sql_server', 'sql', 'schema', 'drop', 'transfer']
)
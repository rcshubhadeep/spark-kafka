from distutils.core import setup
from setuptools import find_packages

from tkf import __project__, __version__

# The requires list is formatted with the best practice written here -
# https://packaging.python.org/requirements/#install-requires

# You ask why six is here? Because - https://github.com/pypa/pip/issues/3165
requires = [
    'avro-python3>=1.8.2',
    'confluent-kafka>=0.11.0',
    'fastavro>=0.17.9',
    'fire>=0.1.3',
    'pyspark>=2.3.0'
]

if __name__ == "__main__":
    setup(
        name=__project__,
        version=__version__,
        packages=find_packages(),
        author='Shubhadeep Roychowdhury',
        author_email='shubhadeeproychowdhuy@gmail.com',
        install_requires=requires,
        description='Example application to use Kafka and Avro and others',
        include_package_data=True,
    )

from setuptools import setup, find_packages

setup(
    name='waxtion',
    version='0.1.8',
    description='A transaction signer and table fetcher on wax made easier.',
    url='https://github.com/funkaclau',
    author='funkaclau',
    packages=find_packages(),
    install_requires=[
        "pyntelope"
    ],
)

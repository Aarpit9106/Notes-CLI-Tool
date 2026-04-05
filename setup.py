
from setuptools import setup, find_packages

setup(
    name='notes-cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=8.1.7',
        'rich>=13.7.0',
    ],
    entry_points={
        'console_scripts': [
            'notes=notes.cli:cli',
        ],
    },
)

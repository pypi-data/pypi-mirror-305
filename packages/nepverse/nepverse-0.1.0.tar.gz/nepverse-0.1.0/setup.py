
from setuptools import setup, find_packages

setup(
    name='nepverse',  # The name of your package
    version='0.1.0',  # Initial version
    author='Nepcoder',  # Your name
    author_email='',  # Your email
    description='A simple API wrapper for Nepcoder tools.',  # Short description
    long_description=open('README.md').read(),  # Long description read from README file
    long_description_content_type='text/markdown',
    url='https://github.com/Nepcoder0981',  # URL to your project's GitHub repository
    packages=find_packages(),  # Automatically find and include packages
    install_requires=open('requirements.txt').read().splitlines(),  # List of dependencies
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)

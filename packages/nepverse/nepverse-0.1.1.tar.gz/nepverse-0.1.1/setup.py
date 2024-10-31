from setuptools import setup, find_packages

setup(
    name='nepverse',
    version='0.1.1',  # Increment version number here
    description='A simple wrapper for Nepcoder API for search functionalities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nepcoder',
    author_email='your.email@example.com',
    url='https://pypi.org/project/nepverse/',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

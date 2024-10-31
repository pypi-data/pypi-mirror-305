from setuptools import setup, find_packages

setup(
    name="nepverse",
    version="0.1.2",
    author="Nepcoder",
    author_email="nepcoder@example.com",  # Change to your email if needed
    description="A simple API wrapper for Nepcoder tools.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nepcoder0981/nepverse",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

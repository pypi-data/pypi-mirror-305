from setuptools import setup, find_packages

setup(
    name="nepverse",
    version="0.1.3",
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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
)

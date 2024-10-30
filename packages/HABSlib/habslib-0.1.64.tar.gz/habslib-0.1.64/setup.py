from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="HABSlib",
    version="0.1.64",
    author="Domenico Guarino",
    author_email="domenico@habs.ai",
    description="A library for interacting with the HABS CognitiveOS API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Olocufier/HABS.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "asyncio==3.4.3",
        "brainflow==5.12.1",
        "numpy==1.26.4",
        "requests==2.31.0",
        "urllib3==2.2.1",
        "jsonschema",
        "rfc3339-validator",
        "scipy",
        "pytest",
        "pytest-html",
        "pytest-order",
        "pytest-dependency",
        "pdoc",
        "pyEDFlib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[('docs', ['docs/index.html'])],
    license="MIT",
    python_requires='>=3.6',
)

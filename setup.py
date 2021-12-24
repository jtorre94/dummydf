import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="dummydf",
    version="0.0.3",
    description="Generate a dummy dataframe for testing",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jtorre94/dummydf",
    author="torre.preciado",
    author_email="torre.preciado@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['dummydf'],
    install_requires=[
        'numpy==1.21.5',
        'pandas==1.3.5',
        'PyYAML==6.0'
    ],
)

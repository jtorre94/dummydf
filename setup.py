from setuptools import setup

setup(
    name='dummydf',
    version='0.0.1',
    packages=['dummydf'],
    install_requires=[
        'numpy',
        'pandas; python_version == "3.7.4"',
    ],
)

from setuptools import setup

setup(
    name='dummydf',
    version='0.0.1',
    packages=['dummydf'],
    install_requires=[
        'numpy',
        'pandas',
        'PyYAML'
    ],
    package_data=[('', ['dummydf/config/config_dummydf.yml'])],
)

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
    data_files=[('config', ['dummydf/blob/main/dummydf/config/config_dummydf.yml'])],
)

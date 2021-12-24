from setuptools import setup

setup(
    name='dummydf',
    version='0.0.1',
    packages=['dummydf'],
    install_requires=[
        'numpy==1.21.5',
        'pandas==1.3.5',
        'PyYAML==6.0'
    ],
    include_package_data=True,
)

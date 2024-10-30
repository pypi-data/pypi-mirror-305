from setuptools import setup, find_packages

setup(
    name='vassure',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'selenium',
        'pytest-xdist',     # For parallel execution
        'pytest-html',      # For HTML reporting
        'pyyaml',           # For configuration handling
        'logger',
        'bson',
        'pymongo',
        'pycryptodome',
        'robotframework-pabot',
        'robotframework-seleniumlibrary',
        'pytz',
        'requests',
        'ratelimit',
    ],
    entry_points={
        'console_scripts': [
            'pytest-selenium=pytest:main'
        ]
    },
)

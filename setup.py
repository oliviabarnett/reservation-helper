from setuptools import setup, find_packages

setup(
    name='reservationHelper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'openai',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'reservation-helper=flaskr:app'
        ]
    }
)
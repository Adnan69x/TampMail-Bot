from setuptools import setup, find_packages

setup(
    name='TempMail-Bot',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'aiogram==2.21',
        'requests==2.28.1',
        'beautifulsoup4==4.11.1'
    ],
)

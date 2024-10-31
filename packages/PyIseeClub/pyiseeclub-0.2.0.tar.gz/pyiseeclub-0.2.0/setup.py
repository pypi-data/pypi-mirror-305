# setup.py

from setuptools import setup, find_packages

setup(
    name='PyIseeClub',
    version='0.2.0',
    packages=find_packages(),
    description='isee club is public library',
    author='Isee',
    author_email='',
    url='',  # GitHub 链接
    install_requires=[
        'pytz==2024.2',
        'sshtunnel==0.4.0',
        'PyMySQL==1.1.1',
        'SQLAlchemy==2.0.32',
        'redis==5.2.0',
    ],
)

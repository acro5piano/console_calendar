import imp
import os
from setuptools import setup, find_packages

version = imp.load_source(
    'version', os.path.join('caravel', 'version.py'))

setup(
    name='console_calendar',
    description=("A calendar working in console."),
    version=version.VERSION_STRING,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=['console_calendar/bin/console_calendar'],
    install_requires=[
        'parsedatetime==2.0.0',
        'python-dateutil==2.5.3',
    ],
    # extras_require={
    #     'cors': ['Flask-Cors>=2.0.0'],
    # },
    tests_require=[
        'pytest',
    ],
    author='Kazuya Gosho',
    author_email='ketsume0211@gmail.com',
    url='',
    # download_url=(
    #     'https://github.com/airbnb/caravel/tarball/' + version.VERSION_STRING),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

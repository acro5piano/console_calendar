import imp
import os
from setuptools import setup, find_packages

version = imp.load_source(
    'version', os.path.join('console_calendar', 'version.py'))

setup(
    name='console_calendar',
    description=("A calendar working in console."),
    version=version.VERSION_STRING,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=['console_calendar/bin/concal'],
    install_requires=[
        'termcolor',
    ],
    tests_require=[
        'ipython',
        'pytest',
    ],
    author='Kazuya Gosho',
    author_email='ketsume0211@gmail.com',
    url='https://github.com/acro5piano/console_calendar',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

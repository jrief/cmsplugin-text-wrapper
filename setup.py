import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmsplugin-text-wrapper",
    version = "0.6",
    url = 'https://github.com/jrief/cmsplugin-text-wrapper',
    license = 'BSD',
    description = "A django-cms plugin which extends and replaces the shipped text plugin with simple wrapper functionalities.",
    long_description = read('README.rst'),
    author = 'Jacob Rief',
    author_email = 'jacob.rief@gmail.com',
    packages = find_packages(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "Django >= 1.3",
        "django-cms >= 2.3",
    ],
    include_package_data=True,
    zip_safe = False,
)

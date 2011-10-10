import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django_structurer",
    version = "0.0.7",
    author = "Felipe Arruda Pontes",
    author_email = "contato@arruda.blog.br",
    description = ("This app allow you to create your own custom django project structure, and then use it as you please."),
    license = "MIT",
    keywords = "django project structure",
    url = "http://packages.python.org/django_structurer",
    packages=['django_structurer'],
    scripts = ['django_structurer/bin/djstruct.py'],
    data_files = ['django_structurer/default_structure.yaml',
                  'django_structurer/snippets',],
    install_requires=[
        'PyYAML==3.09'
    ],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
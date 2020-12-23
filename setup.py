import io
import os
import re

from setuptools import find_packages
from setuptools import setup

import versioneer


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="haccytrees",
    version=versioneer.get_version(),
    url="none",
    license='MIT',

    author="Michael Buehlmann",
    author_email="buehlmann.michi@gmail.com",

    description="None",
    long_description=read("README.rst"),

    cmdclass=versioneer.get_cmdclass(),

    packages=find_packages(exclude=('tests', 'executables')),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
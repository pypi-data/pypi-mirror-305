import io
import os

from setuptools import setup

# The text of the README file
here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name="aiokwikset",
    version="0.3.0a2",
    description="Python interface for Kwikset Smart Locks",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/explosivo22/aiokwikset",
    author="Brad Barbour",
    author_email="barbourbj@gmail.com",
    license='Apache Software License',
    install_requires=[ 'aiohttp', 'pycognito' ],
    keywords=[ 'kwikset', 'home automation', 'kwikset halo', 'kwikset smart lock' ],
    packages=[ 'aiokwikset' ],
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
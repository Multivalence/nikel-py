from setuptools import setup
from codecs import open
from os import path


# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="nikel-py",
    version="0.1.7",
    description="Python API Wrapper for the Nikel API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Multivalence/nikel-py",
    author="Multivalence",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'


    ],
    packages=["nikel_py", "nikel_py.utils"],
    include_package_data=True,
    install_requires=['requests','aiohttp', 'python-dateutil'],
    python_requires='>=3.6.0'
)
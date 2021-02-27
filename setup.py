import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


version_contents = {}
with open("ledgerx/version.py", "r", encoding="utf-8") as f:
    exec(f.read(), version_contents)


with open("README.md", "r") as f:
    long_description = f.read()


dependencies = [
    "requests>=2.20.0",
    "Deprecated",
]


test_dependencies = ["pytest", "black"]


setup(
    name="ledgerx",
    version=version_contents["VERSION"],
    description="python client for ledgerx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Weston Platter",
    author_email="westonplatter@gmail.com",
    url="https://github.com/westonplatter/lederx-python/",
    license="BSD-3-Clause",
    python_requires=">=3.6",
    packages=["ledgerx"],
    # package_data={'fast_arrow': ['ssl_certs/certs.pem']},
    install_requires=dependencies,
    tests_require=test_dependencies,
    project_urls={
        "Issue Tracker": "https://github.com/westonplatter/ledgerx-python/issues",
        "Source Code": "https://github.com/westonplatter/ledgerx-python",
    },
)

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass into pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = "-n auto"

    def run_tests(self):
        import shlex
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


version_contents = {}
with open("ledgerx/version.py", "r", encoding="utf-8") as f:
    exec(f.read(), version_contents)


with open("README.md", "r") as f:
    long_description = f.read()


deps = [
    "requests>=2.20.0",
]


test_deps = ["pytest", "black"]


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
    install_requires=deps,
    tests_require=test_deps,
    cmdclass={"test": PyTest},
    project_urls={
        "Issue Tracker": "https://github.com/westonplatter/ledgerx-python/issues",
        "Source Code": "https://github.com/westonplatter/ledgerx-python",
    },
)

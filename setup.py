from setuptools import setup, find_packages

setup(
    name="curldrop",
    version="1.0.5",
    packages=find_packages(),
    author="Kevin Kennell",
    author_email="kevin@kennell.de",
    license="MIT",
    url="http://github.com/kennell/curldrop",
    install_requires=["flask", "click", "gunicorn", "six"],
    entry_points={"console_scripts": ["curldrop = curldrop.cli:main"]},
)

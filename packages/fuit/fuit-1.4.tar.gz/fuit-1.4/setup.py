from setuptools import setup

libs = open("requirements.txt").read().splitlines()
description = open("README.md", encoding="utf-8").read()
setup(
    name="fuit",
    version="1.4",
    url="",
    license="MIT",
    author="DaSh-More",
    author_email="",
    description="FU IT&ABD",
    long_description=description,
    long_description_content_type="text/markdown",
    install_requires=libs,
    platforms=["any"],
)

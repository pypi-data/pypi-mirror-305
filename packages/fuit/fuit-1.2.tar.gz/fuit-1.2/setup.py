from setuptools import setup

libs = open("requirements.txt").read().splitlines()
description = open("README.md", encoding="utf-8").read()
setup(
    name="fuit",
    version="1.2",
    url="",
    license="MIT",
    author="DaSh-More",
    author_email="",
    description=description,
    install_requires=libs,
    platforms=["any"],
)

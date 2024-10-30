from setuptools import setup

libs = open("requirements.txt").read().splitlines()
setup(
    name="fuit",
    version="1.0",
    url="",
    license="MIT",
    author="DaSh-More",
    author_email="",
    description="",
    install_requires=libs,
    platforms=["any"],
)

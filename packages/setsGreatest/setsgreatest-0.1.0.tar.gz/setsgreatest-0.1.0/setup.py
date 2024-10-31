from setuptools import setup, find_packages

setup(
    name="setsGreatest",                    # Package name
    version="0.1.0",                      # Version
    packages=find_packages(),  
                          # Automatically find packages
    description="Find the greatest value among a bunch of numbers via my Logic using sets and lists",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="SIDAGANA UDAY",
    author_email="uday.sidgana@gmail.com",


)
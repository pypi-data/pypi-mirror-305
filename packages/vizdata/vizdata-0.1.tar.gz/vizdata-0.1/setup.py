from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name="vizdata",
      version="0.1",
      description="Simple Exploratory Data Analysis tool.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/darkhan-ai/vizdata",
      license="MIT",
      packages=["vizdata"],
      zip_safe=False)

from setuptools import setup

def  readme_file():
      with open("README.rst", encoding="utf-8") as rf:
            return rf.read()
setup(name="tyfabu", version="1.0.0", description="this is a niubi lib", package=["tyfabu1"], py_modules=["tool"], author="ty", author_email="1003144926@qq.com",
      long_description=readme_file(), url="https://github.com/ty/python_code")
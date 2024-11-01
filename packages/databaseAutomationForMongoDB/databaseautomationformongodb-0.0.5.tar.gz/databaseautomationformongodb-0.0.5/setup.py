from setuptools import setup, find_packages
from typing import List

'''def get_requirement(file_path:str)->List:
      requirements = []
      with open(file_path) as f:
          requirements = f.readlines()
          requirements = [req.replace("\n", "") for req in requirements]

          if HYPEN_E_DOT in requirements:
              requiements.remove(HYPEN_E_DOT)
    return requirements'''

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.5"
REPO_NAME = "AutomaedMongoDBConnectorPckg"
PKG_NAME= "databaseAutomationForMongoDB"
AUTHOR_USER_NAME = "Anant4830"
AUTHOR_EMAIL = "anant4830@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    #if above requiement def function get_requirement is executed then give this alos a parameter
    #install_requires = get_requirement("./requirements_dev.txt"),
    )
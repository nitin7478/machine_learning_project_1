from setuptools import setup,find_packages
from typing import List



# declaring variables for setup function
PROJECT_NAME = "housung-predictor"
VERSION = "0.0.4"
AUTHOR="Nitin Udmale"
DESCRIPTION="This is my first machine learning project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description : This fucntion is going to return list of requirement mentioned in
    requirements.txt file 
    
    Return :  This function is going to return a list which contain name
    of libraries mentioned is requirements.txt file 
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), #return all the packages with __init__.py file in it
install_requires = get_requirements_list()
)

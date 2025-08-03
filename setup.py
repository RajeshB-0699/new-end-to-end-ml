from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(filepath: str)-> List[str]:
    requirements = []
    with open(filepath) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlProject1',
    author="Rajesh B",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
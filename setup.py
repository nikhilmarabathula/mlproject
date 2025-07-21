from setuptools import find_packages, setup
from typing import List

HYPHEN_DOT_E = '-e .'

def get_requirements(file_name: str) -> List[str]:
    with open(file_name) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Nikhil',
    author_email='nikhilmara123@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)

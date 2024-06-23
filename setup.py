# # automatically finds all the packages that we have used or created in our enitre project
# from setuptools import find_packages, setup


# setup(
#     name='dsdemo',
#     version='0.0.1',    # wheneven my nextversion comes we can update it and entire pacages will be built and going to pypi, where others can also use it
#     author='saranya'
#     author_email='gvnlsaranya2003.gmail.com'
#     packages=find_packages(),
#     install_requires=['pandas', 'numpy', 'seaborn']
# )











# from setuptools import find_packages, setup
# from typing import List

# HYPEN_E_DOT = '-e .'


# def get_requirements(file_path: str) -> List[str]:
#     '''
#     this function will return the list of requirements
#     '''

#     requirements = []
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.replace("\n", " ") for req in requirements]
#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
#     return requirements


# setup(
#     name='dsdemo',
#     version='0.0.1',
#     author='saranya',
#     author_email='gvnlsaranya2003@gmail.com',  # corrected email format
#     packages=find_packages(),
#     # install_requires=['pandas', 'numpy', 'seaborn']    # we cant write all packages like this
#     install_requires=get_requirements('requirements.txt')
# )








from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path):
    '''
    Function to parse requirements.txt file and return list of requirements.
    '''
    with open(file_path, 'r') as file:
        requirements = [line.strip() for line in file.readlines() if line.strip()]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='dsdemo',
    version='0.0.1',
    author='saranya',
    author_email='gvnlsaranya2003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)

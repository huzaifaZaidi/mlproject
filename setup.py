from setuptools import setup, find_packages
from typing import List
hypen_e_dot='-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    This Func will return list of requirements
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    description='A short description of your project',
    author='huzaifaZaidi',
    author_email='huzaifahmedzaidi@gmail.com',
#     url='https://github.com/yourusername/your_project_name',  # if applicable
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=get_requirements('requirements.txt')
#     install_requires=[
#         'numpy',  # Add your dependencies here
#         'pandas',
#         'matplotlib',
#         'jupyter','seaborn']
# #     classifiers=[
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],
#     python_requires='>=3.6',  # Specify Python version compatibility
)

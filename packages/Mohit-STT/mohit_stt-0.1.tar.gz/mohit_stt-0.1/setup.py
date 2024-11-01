from setuptools import setup,find_packages

setup(
    name = 'Mohit_STT' ,
    version = '0.1' ,
    author= 'Mohit Kumar',
    author_email='megamohit2006@gmail.com',
    description='This is speech to text package created by Mohit Kumar'
)

packages = find_packages(),
install_reqirements=[
    'selenium',
    'webdriver_manager'
]
from setuptools import setup, find_packages

setup(
    name='my-python-project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # add your project dependencies here
        # for example: 'numpy>=1.11.1'
    ],
    entry_points={
        'console_scripts': [
            # add cli commands here
            # for example: 'my-command = my_python_project.main:main'
        ],
    },
)
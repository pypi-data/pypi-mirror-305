from setuptools import setup, find_packages

setup(
    name='ratify',
    packages=find_packages(),
    version='0.2.0',
    description='A simple validation library',
    author='tobiy23@gmail.com',
    python_requires='>=3.6',
    install_requires=[
        're',
        'datetime',
        'jsonschema'
    ]
)

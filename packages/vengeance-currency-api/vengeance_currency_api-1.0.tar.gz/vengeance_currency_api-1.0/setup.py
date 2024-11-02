# setup.py
from setuptools import setup, find_packages

setup(
    name='vengeance-currency-api',
    version='1.0',
    author='Preetham Kamishetty',
    author_email='kamishettypreetham@gmail.com',
    description='A RESTful API for currency symbols and codes for countries across the world.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/preetham-1811/currency-api',  # Replace with your repo URL
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

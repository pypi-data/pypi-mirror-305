# setup.py

from setuptools import setup, find_packages

setup(
    name='nepbot',
    version='0.1',
    author='Your Name',  # Replace with your name
    author_email='your_email@example.com',  # Replace with your email
    description='A package to interact with a custom AI model API',
    packages=find_packages(),
    install_requires=[
        'requests',  # Dependency for making HTTP requests
    ],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Ensures compatibility with Python 3.6 and above
)

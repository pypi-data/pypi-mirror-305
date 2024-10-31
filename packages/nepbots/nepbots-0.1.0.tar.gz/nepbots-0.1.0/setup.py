from setuptools import setup, find_packages

setup(
    name='nepbots',  # Name of your package
    version='0.1.0',  # Initial version
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        'requests',  # List of dependencies
    ],
    author='t.me/nepcoderapis',  # Your name
    author_email='your.email@example.com',  # Your email
    description='A simple API wrapper for Nepbots',  # Short description
    long_description=open('README.md').read(),  # Detailed description from README file
    long_description_content_type='text/markdown',  # Format of long description
    url='https://github.com/Nepcoder0981',  # URL to your project (if available)
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)

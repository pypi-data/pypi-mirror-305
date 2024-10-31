from setuptools import setup, find_packages

setup(
    name='nepbots',  # The name of your package
    version='0.1.1',  # Version of your package
    author='t.me/nepcoder',  # Replace with your name
    author_email='your_email@example.com',  # Replace with your email
    description='A simple API wrapper for interacting with Nepbots API',
    long_description=open('README.md').read(),  # Optional: Long description read from README
    long_description_content_type='text/markdown',  # Optional: Content type of long description
    url='https://github.com/yourusername/nepbots',  # Optional: URL to your project
    packages=find_packages(),  # Automatically find packages in the directory
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',  # Adjust based on your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
    install_requires=[
        'requests',  # Dependencies your package requires
    ],
)

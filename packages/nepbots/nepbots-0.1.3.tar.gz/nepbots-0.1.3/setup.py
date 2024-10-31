from setuptools import setup, find_packages

# Define package metadata
VERSION = "0.1.3"  # Updated package version
DESCRIPTION = "A simple API client for Nepbots"  # Short description

setup(
    name="nepbots",  # The name of your package
    version=VERSION,  # Version number
    author="NePCoder",  # Updated author name
    author_email="your.email@example.com",  # Your email
    description=DESCRIPTION,  # A short description
    long_description_content_type="text/markdown",  # Content type for long description
    long_description="",  # Removed the long description (as README.md is not used)
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=['requests'],  # Dependencies for your package
    keywords=['python', 'api', 'nepbots'],  # Keywords for your package
    classifiers=[
        "Development Status :: 3 - Alpha",  # Status of the package
        "Intended Audience :: Developers",  # Target audience
        "Programming Language :: Python :: 3",  # Supported Python versions
        "Operating System :: OS Independent",  # OS independence
        "Environment :: Console",  # Environment in which the package is expected to be used
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
)

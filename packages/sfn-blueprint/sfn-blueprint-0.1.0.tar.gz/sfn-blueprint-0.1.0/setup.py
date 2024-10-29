# Setup file for pip installation
# Setup file for pip installation

from setuptools import setup, find_packages

# To Load the README file to use as the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sfn-blueprint",
    version="0.1.0",  # Initial release version
    author="Rajesh Darak",
    author_email="rajesh@stepfuction.ai",
    description="sfn-blueprint is a modular framework that provide rapid development of AI Agents and easy to Customize",
    long_description=long_description,  # Using README.md as long description
    long_description_content_type="text/markdown",  # README file format
    url="https://github.com/iamrajeshdaraksfn/sfn_blueprint",  # Github URL
    packages=find_packages(),  # This will Automatically find and include packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # License
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # Required Python version
    install_requires=[
        # List of dependencies required for this package
        'pandas==1.5.3',
        'numpy==1.24.3',
        'openai==1.40.3',
        'python-dotenv==1.0.0',
        'streamlit==1.39.0',
        'PyYAML==6.0'
    ]
)
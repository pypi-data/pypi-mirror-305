from setuptools import setup, find_packages

setup(
    name="mruus-lib",  # Replace with your package name
    version="0.1.0",    # Update the version as needed
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        # List your package dependencies here
        'setuptools',
        'wheel'
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A common library for my Django projects",
    long_description=open("README.md").read(),  # Read long description from README
    long_description_content_type="text/markdown",
    url="https://github.com/mruus/mruus-lib",  # Repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify your Python version requirements
)

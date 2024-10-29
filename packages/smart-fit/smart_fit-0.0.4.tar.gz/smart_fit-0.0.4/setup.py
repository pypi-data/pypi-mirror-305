from setuptools import setup, find_packages

setup(
    name="smart_fit",  # Choose a unique name for your library
    version="0.0.4",
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-library",  # Project URL
    packages=find_packages(),  # Automatically find packages in `my_library/`
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",  # Specify minimum Python version
    install_requires=[
        # List your library dependencies here
    ],
)
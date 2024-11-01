from setuptools import setup, find_packages

setup(
    name="end_of_distribution",
    version="0.1.0",
    author="Aditya Yadav",
    author_email="aditya.yadav.bse@gmail.com",
    description="A Python library for detecting outliers at the end of the distribution",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/adityayadav0111/end_of_distribution",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

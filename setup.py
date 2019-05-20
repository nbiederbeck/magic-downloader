from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="MAGICDownloader",
    author="Noah Biederbeck",
    author_email="noah.biederbeck@tu-dortmund.de",
    version="0.1.1",
    description="Download MAGIC data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["requests", "bs4", "tqdm", "lxml"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)

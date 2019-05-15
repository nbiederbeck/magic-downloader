from setuptools import setup, find_packages

setup(
    name="MAGICDownloader",
    author="Noah Biederbeck",
    author_email="noah.biederbeck@tu-dortmund.de",
    version="0.1.0",
    description="Download MAGIC data",
    packages=find_packages(),
    install_requires=["requests", "bs4", "tqdm", "lxml"],
)

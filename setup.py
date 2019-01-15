from setuptools import setup, find_packages

setup(
    name="timing_magic_fact",
    author="Noah Biederbeck",
    author_email="noah.biederbeck@tu-dortmund.de",
    version="0.1",
    description="Compare timing information from the IACTs MAGIC and FACT",
    packages=find_packages(),
    install_requires=["requests", "bs4", "tqdm"],
)

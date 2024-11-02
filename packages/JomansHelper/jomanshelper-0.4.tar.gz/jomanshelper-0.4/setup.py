from setuptools import setup, find_packages

setup(
    name="JomansHelper",
    version="0.4",  
    packages=find_packages(),
    description="Jomans Helper",
    author="Dein Name",
    install_requires=["colorama", "psutil", "fake_useragent"],
)

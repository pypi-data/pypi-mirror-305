from setuptools import setup, find_packages

setup(
    name="JomansHelper",
    version="0.2",
    packages=find_packages(), 
    description="Jomans Helper",
    author=".joman21.",
#    author_email="deinname@example.com",
    install_requires=["colorama", "psutil","platform","fake_useragent"],
)

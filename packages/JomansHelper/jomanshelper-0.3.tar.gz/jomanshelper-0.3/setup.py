from setuptools import setup, find_packages

setup(
    name="JomansHelper",
    version="0.3",  # Erhöhe die Versionsnummer hier auf eine neue, unbenutzte Version
    packages=find_packages(),
    description="Jomans Helper",
    author="Dein Name",
    install_requires=["colorama", "psutil", "platform", "fake_useragent"],
)


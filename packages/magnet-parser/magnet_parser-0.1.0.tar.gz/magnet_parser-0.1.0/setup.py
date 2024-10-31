from setuptools import setup, find_packages

setup(
    name="magnet-parser",
    version="0.1.0",
    description="A module for decoding and encoding magnet URIs.",
    author="Muhammad Al Fajri",
    author_email="admin@pyjri.com",
    packages=find_packages(),
    install_requires=[
        # List any dependencies your module needs
    ],
    entry_points={
        'console_scripts': [
            'magnet=magnet_parser.magnet:main',  # Assuming you will create a main function later
        ],
    },
)
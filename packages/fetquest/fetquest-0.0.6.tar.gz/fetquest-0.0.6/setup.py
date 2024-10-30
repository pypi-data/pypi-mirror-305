from setuptools import setup, find_packages
from pathlib import Path
import setuptools
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name = "fetquest",
    version = "0.0.6",
    author = "Dhinesh Palanisamy",
    author_email = "daps.investment@gmail.com",
    description = "Package to help on Stock Market Visualization and Data",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['yfinance', 'pandas', 'plotly.express'],
    packages = find_packages(exclude=['contrib', 'docs', 'tests', 'examples'])

)
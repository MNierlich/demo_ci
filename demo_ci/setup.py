from setuptools import setup, find_packages
from demo_ci import __version__

setup(
    name="demo_ci",
    version=__version__,
    description="A demo Python package",
    author="Michael Nierlich",
    author_email="Michael.Nierlich@grob.de",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
)

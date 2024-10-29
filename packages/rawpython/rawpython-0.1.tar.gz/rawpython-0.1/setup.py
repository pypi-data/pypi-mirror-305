from setuptools import setup
from pathlib import Path

readme = Path(__file__).parent / 'README.md'

with open(readme) as f:
    description = '\n'.join([line for line in f][2:])

setup(
    name='rawpython',
    version='0.1',
    description="a library for people who hate libraries",
    long_description=description,
    author='Diego Llanes',
    author_email='rawpython@diegollanes.com',
)

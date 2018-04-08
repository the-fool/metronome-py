from setuptools import setup, find_packages

setup(
    name='python-package-example',
    version='1',
    packages=find_packages(),
    license='MIT',
    description='A simple metronome',
    long_description=open('README.md').read(),
    url='https://github.com/the-fool/metronome-py',
    author='Thomas Ruble',
    author_email='tr@thomasruble.com'
)

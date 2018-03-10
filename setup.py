try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='codetimer',
    version='1.0.0',
    packages=['codetimer'],
    url='https://github.com/gulaki/code-timer',
    license='MIT',
    author='Anustuv',
    author_email='anustuv@gmail.com',
    description='A library of methods to time code paths and functions in a flexible way.'
)

import os

from setuptools import find_packages, setup

version_contents = {}
version_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'opentranslator/version.py'
)

with open(version_path, 'rt') as f:
    exec(f.read(), version_contents)

with open('README.md', 'r') as fh:
    long_description = fh.read()


with open('requirements.txt', 'r') as f:
    requirements = f.read().split('\n')

setup(
    name='opentranslator',
    description='Python client library for translate text with OpenAI API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=version_contents['VERSION'],
    install_requires=requirements,
    python_requires='>=3.7',
    include_package_data=True,
    scripts=['bin/opentranslator'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    author='FabrizioCafolla',
    author_email='developer@fabriziocafolla.com',
    url='https://github.com/fabriziocafolla/opentranslator',
)

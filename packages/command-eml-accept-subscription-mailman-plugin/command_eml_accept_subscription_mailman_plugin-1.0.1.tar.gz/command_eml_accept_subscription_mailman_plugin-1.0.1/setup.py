from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='command-eml-accept-subscription-mailman-plugin',
    version='1.0.1',
    packages=find_packages('.'),
    description='Plugin that add a command to accept a subscription request to mailing list by email',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Tann-dev/command-eml-accept-subscription-mailman-plugin',
    author='Tann-dev',
    author_email='snakestone@myyahoo.com',
    install_requires = [
        'mailman',
        'atpublic',
    ]
)
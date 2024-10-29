from setuptools import setup, find_packages


setup(
    name='command-eml-accept-subscription-mailman-plugin',
    version='0.0.1',
    packages=find_packages('.'),
    description='Plugin that add a command to accept a subscription request to mailing list by email',
    long_description='Plugin that add a command to accept a subscription request to mailing list by email',
    url='https://github.com/Tann-dev/command-eml-accept-subscription-mailman-plugin',
    author='Tann-dev',
    author_email='snakestone@myyahoo.com',
    install_requires = [
        'mailman',
        'atpublic',
    ]
)
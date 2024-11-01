from setuptools import setup, find_packages

setup(
    name='ApaDown',
    version='1.0.0',
    description='Download Files hosted in an Apache Server',
    author='DJEBARRA Rabah Abderrazak',
    author_email='djebarra.ra@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'tqdm',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'apadown = ApaDown.cli:main',
        ],
    },
)
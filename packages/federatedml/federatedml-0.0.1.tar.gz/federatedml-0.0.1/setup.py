from setuptools import setup, find_packages

setup(
    name='federatedml',
    version='0.0.1',
    author='Kerem Bayramoğlu',
    author_email='kerembay9@gmail.com',
    description='federated learning package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[

    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
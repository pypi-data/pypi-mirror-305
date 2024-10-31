from setuptools import setup, find_packages

setup(
    name='nathan_cohn_calculator',
    version='0.1.0',
    author='Nathan Cohn',
    author_email='nathan@example.com',
    description='A simple calculator package',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

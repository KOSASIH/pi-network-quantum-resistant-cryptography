import os
from setuptools import setup, find_packages

# Get the long description from the README.md file
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

# Get the version number from the __init__.py file
with open(os.path.join(os.path.dirname(__file__), 'src', 'piquantum', '__init__.py')) as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip().strip('"')
            break

# Define the setup function
setup(
    name='PiQuantum',
    version=version,
    description='A high-tech cryptography library for secure communication.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/piquantum/piquantum',
    author='PiQuantum Team',
    author_email='support@piquantum.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Security :: Cryptography',
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.7',
    install_requires=[
        'cryptography>=3.4.7',
        'pycryptodome>=3.15.0',
        'pycryptodomex>=3.15.0',
        'pycrypt>=2.6',
        'pycryptdk>=2.0.1',
        'pycryptography>=0.2.1',
        'pycryptix>=0.5',
        'pycryptopp>=0.6.1',
        'pyopenssl>=21.0.0',
    ],
    extras_require={
        'test': [
            'pytest>=6.2.5',
            'pytest-cov>=3.0.0',
            'pytest-sugar>=0.9.4',
            'pytest-xdist>=2.5.0',
            'pytest-benchmark>=3.4.1',
        ],
    },
    entry_points={
        'console_scripts': [
            'piquantum = piquantum.cli:main',
        ],
    },
)

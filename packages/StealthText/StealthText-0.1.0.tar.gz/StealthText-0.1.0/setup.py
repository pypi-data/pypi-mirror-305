from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='StealthText',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'cryptography',
    ],
    description='A simple encryption and decryption library for secure messaging.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='MrFidal',
    author_email='mrfidal@proton.me',
    url='https://github.com/ByteBreach/StealthText',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'stealthtext=stealthtext.cli:main',
        ],
    },
)

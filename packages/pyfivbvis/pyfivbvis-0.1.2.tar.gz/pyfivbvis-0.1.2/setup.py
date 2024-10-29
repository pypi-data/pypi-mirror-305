from setuptools import setup, find_packages

setup(
    name='pyfivbvis',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'pyfivbvis=pyfivbvis:main',  # Adjust based on your package
        ],
    },
    author='Tyler Widdison',
    author_email='tylerperrywiddison@gmail.com',
    description='A Python package to fetch data from FIVB VIS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/openvolley/pyfivbvis',  # Your GitHub repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

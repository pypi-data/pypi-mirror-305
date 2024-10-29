from setuptools import setup, find_packages

setup(
    name='alex_tech_logging_library',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Tapan Bhatnagar',
    author_email='tapan@alexandriatechnology.com',
    description='A custom logging library built on Python\'s standard logging module. It provides a simple way to set up a logger with file and console handlers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
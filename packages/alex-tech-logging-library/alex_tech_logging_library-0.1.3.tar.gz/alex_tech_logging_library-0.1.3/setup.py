from setuptools import setup, find_packages

#  1. Build the package:   python setup.py sdist bdist_wheel;
#  2. Upload the package to PyPI:  twine upload dist/*;
#  api token :
#  pypi-AgEIcHlwaS5vcmcCJDg4ZDJmMzA4LTI1YTAtNDdjYi1iN2ZhLTk1NTdiZWM0YjRjMwACIVsxLFsiYWxleC10ZWNoLWxvZ2dpbmctbGlicmFyeSJdXQACLFsyLFsiNjQ3YzFmNjAtMzA4Ny00ZGM2LTg5MjgtM2EwYWQ4ZWFjMDRiIl1dAAAGII8XCG5mhX3YKTHOLNdy7wXwDsrXbcyk8exoQheocEBH

#  python setup.py sdist bdist_wheel && twine upload dist/* --verbose
setup(
    name='alex_tech_logging_library',
    version='0.1.3',
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
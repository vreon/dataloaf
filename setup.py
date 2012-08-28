from setuptools import setup, find_packages
from dataloaf import __doc__, __version__

setup(
    name='dataloaf',
    version=__version__,
    author='Jesse Dubay',
    author_email='jesse@thefortytwo.net',
    description=__doc__,
    license='MIT',
    keywords='grammar generator random',
    packages=find_packages(),
    classifiers=[
        'Topic :: Text Processing',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
    ],
)

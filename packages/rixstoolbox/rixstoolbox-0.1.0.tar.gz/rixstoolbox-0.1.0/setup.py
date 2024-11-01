from setuptools import setup

setup(
    name='rixstoolbox',
    version='0.1.0',    
    description='Python package for analysis of ESRF ID32 RIXS data',
    url='https://github.com/kkummer/RixsToolBox',
    author='Kurt Kummer',
    license='MIT',
    packages=['rixstoolbox'],
    install_requires=['numpy'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
    ],
)

from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='ozzymod',
  version='1.0.0',
  description='This Python module is to make your code more readable and shorter.',
  long_description=open('CHANGELOG.txt').read(),
  url='',  
  author='Major Ozzy',
  license='MIT', 
  classifiers=classifiers,
  keywords='modification', 
  packages=find_packages(),
  install_requires=[''] 
)
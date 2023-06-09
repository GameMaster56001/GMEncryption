from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='GMEncryption',
  version='0.0.1',
  description='A new type of way of encoding',
  long_description=open('README.txt').read(),
  url='',  
  author='GM_member229112',
  author_email='hexe82703+alt10@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='encryption', 
  packages=find_packages(),
  install_requires=['string', 'random'] 
)
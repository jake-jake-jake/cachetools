from setuptools import setup, find_packages
 
setup(name='cachetools',
      version='0.1',
      url='https://github.com/the-gigi/pathology',
      license='Apache 2.0',
      author='Jake Davis',
      author_email='jakejakejake@protonmail.com',
      description='Tools for caching expensive calls.',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)


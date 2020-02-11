from setuptools import setup, find_packages

setup(name='tools',
      version='0.1',
      url='https://github.com/the-gigi/pathology',
      license='MIT',
      author='Vincent',
      author_email='',
      description='Daily python tools',
      packages=find_packages(exclude=['test']),
      zip_safe=False)
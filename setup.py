import os
from setuptools import setup

required_modules = []
packages = ['proxy_tools']

setup(name='proxy_tools',
      version='0.1.0',
      description='Proxy Implementation',
      url='http://github.com/jtushman/proxy_tools',
      author='Jonathan Tushman',
      author_email='jonathan@zefr.com',
      install_requires=required_modules,
      license='MIT',
      packages=packages,
      zip_safe=False,
      tests_require=['nose'],
      test_suite='nose.collector',
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          ]
      )

from setuptools import setup, find_packages
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

install_requires = [
    'numpy >= 1.7',
    'matplotlib',
    'future',
    'scipy',
    'colorama'
]

dependency_links = [
    ]


def read(fname):
    return open(os.path.join(BASE_DIR, fname)).read()


setup(name='opto',
      version='0.1',
      description='A Python Toolbox for Optimization',
      url='https://github.com/robertocalandra/opto',
      author='Roberto Calandra',
      author_email='roberto.calandra@berkeley.edu',
      keywords=['optimization', 'science'],
      long_description=read('README.rst'),
      license='LICENSE.txt',
      packages=find_packages(),
      install_requires=install_requires,
      dependency_links=dependency_links,
      zip_safe=True,
      classifiers=[
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      )

from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='pineDOS',
  version='0.0.4',
  author='yaroslav_k',
  description='This library is created to write mini-programms for Pineapple-IV (Imitation of DOS systems)',
  long_description=readme(),
  long_description_content_type='text/markdown',
  packages=find_packages(),
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files pineapple customisible_text custom',
)
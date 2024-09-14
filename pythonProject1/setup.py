from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='speedfile',
  version='0.0.1',
  author='Ilya_A',
  author_email='aleksandrovila815@gmail.com',
  description='Module for project',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'gh repo clone Zerot5/mingw-w64.github.io'
  },
  python_requires='>=3.6'
)
from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='errorLibary',
  version='0.0.6',
  author='dok2412',
  author_email='i@dok2412.ru',
  description='Personal Error Handling Library.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/DoK2412/error_lidrary',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.12',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'https://github.com/DoK2412/error_lidrary'
  },
  python_requires='>=3.12'
)
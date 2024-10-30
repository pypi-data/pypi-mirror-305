from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='datekeeper',
  version='0.0.1',
  author='bogdan_m',
  author_email='bogdanmdosss@gmail.com',
  description='Simple daily event keeper.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/bogdanmishalo/DateKeeper',
  packages=find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='calendar keep date',
  project_urls={
    'GitHub': 'https://github.com/bogdanmishalo/DateKeeper'
  },
  python_requires='>=3.6'
)
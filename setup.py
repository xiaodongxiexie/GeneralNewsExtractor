from setuptools import setup, find_packages
setup(
    name='GeneralNewsExtractor',
    packages=find_packages(exclude=[]),
    version='0.0.1',
    description='General extractor of news pages.',
    author='Kingname',
    author_email='contact@kingname.info',
    url='https://github.com/kingname/GeneralNewsExtractor',
    keywords=['python', 'webcrawler', 'webspider'],
    python_requires='>=3.6',
    license='PyPA',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'License :: PyPA',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
    ]
)
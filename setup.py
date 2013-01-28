from setuptools import setup

CLASSIFIERS = [
    'Programming Language :: Python',
]

version = '0.1'

long_description = file('README.rst').read()
install_requires=[
    'pyzmail', 
]
 
tests_requires=[
]

setup(name='mib.mailtemplates',
      version=version,
      license='Unknown (see LICENSE.txt)',
      author='Andreas Jung',
      author_email='info@zopyx.com',
      maintainer='Andreas Jung',
      maintainer_email='info@zopyx.com',
      classifiers=CLASSIFIERS,
      url='http://pypi.python.org/pypi/mib.mailtemplates',
      description='MIB mail templates',
      long_description=long_description,
      packages=['mib', 'mib.mailtemplates'],
      package_dir = {'': 'src'},
      include_package_data = True,
      zip_safe=False,
      install_requires=install_requires,
      tests_required=tests_requires,
      namespace_packages=['mib'],
      extras_require={
        'testing' : tests_requires,
      },
      entry_points="""\
      """,
      )

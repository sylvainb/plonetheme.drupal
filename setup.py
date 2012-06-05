from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='plonetheme.drupal',
      version=version,
      description="Get all the power of Drupal for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone theme diazo web zope drupal',
      author='Sylvain Boureliou',
      author_email='sylvain.boureliou@gmail.com',
      url='https://github.com/sylvainb/plonetheme.drupal',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'z3c.jbot'
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      },
      )

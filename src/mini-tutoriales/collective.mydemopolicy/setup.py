from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.mydemopolicy',
      version=version,
      description="A demo of Plone Policy product",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='policy product plone telesur website',
      author='Leonardo J. Caballero G.',
      author_email='lcaballero@hoatzin.org',
      url='http://svn.plone.org/svn/collective/spanishdocs/trunk/src/mini-tutoriales/collective.mydemopolicy',
      license='GPL3',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          collective.mydemoapp
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )

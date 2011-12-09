from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='mipaquetepython',
      version=version,
      description="Mi primer paquete python",
      long_description="""\
Mi primer paquete Python""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='paquete python2.6 demo',
      author='Leonardo Caballero',
      author_email='lcaballero@hoatzin.org',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

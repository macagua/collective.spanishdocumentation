from setuptools import setup, find_packages
#
# Note: This file does not really serve any purpose
# it just keeps some tools happy
# 
import os

version = '0.1rc'

setup(name='plone-spanish-documentations',
      version=version,
      description="Spanish Plone Documentation",
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Carlos de la Guardia, Leonardo J. Caballero G. & Plone community contributors',
      author_email='carlos.delaguardia@gmail.com, leonardocaballero@gmail.com',
      url='http://plone.org.ve',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

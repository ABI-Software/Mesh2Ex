from setuptools import setup, find_packages

requirements = ['MeshParser']

long_description = """A Python library that converts a mesh from MeshParser to ex format.
"""

setup(name=u'mesh2ex',
      version='0.1.0',
      description='Convert mesh to ex format.',
      long_description=long_description,
      classifiers=[],
      author=u'Hugh Sorby',
      author_email='',
      url='https://github.com/ABI-Software/Mesh2Ex',
      license='Apache',
      packages=find_packages('src', exclude=['tests', 'tests.*', ]),
      package_dir={'': 'src'},
      zip_safe=True,
      install_requires=requirements,
      )

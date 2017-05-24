
=========
Mesh 2 Ex
=========

A Python library that converts a mesh from MeshParser to ex format.

Usage
=====

::

  from mesh2ex import convert

  # The convert function takes as an input mesh a dict with two keys: 'nodes', and 'elements'  these two keys are given the data taken from a MeshParser Parser class.
  # This function has two optional parameters: style_old, for working with older versions of ex format (currently unused); define_faces, this parameter will additionally define the face elements of higher order elements to surfaces will be visible immediately when creating a surface graphic.
  convert(input_mesh={'nodes': <your nodes/points>, 'elements': <your elements>}, output_ex='your output file')
  
The following is a full example of using MeshParser and Mesh2Ex together::

  from meshparser import parser
  from mesh2ex import convert
  
  p = parser()
  p.parse('file/to/parse.stl')
  
  mesh = {'nodes': p.getPoints(pared=True), 'elements': p.getElements(pared=True, zero_based=True)}
  convert(input_mesh=mesh, output_ex='file/mesh.exfile', define_face=True)

import unittest

from meshparser.stlparser.parser import STLParser
from meshparser.parser import MeshParser
from mesh2ex.mesh2ex import convert


class ParserTestCase(unittest.TestCase):

    def testConvert(self):
        v = STLParser()
        v.parse('data/pelvis_minimal.stl')
        nodes = v.getPoints(pared=True)
        self.assertEqual(13, len(nodes))
        elements = v.getElements(zero_based=False, pared=True)
        self.assertEquals([1, 4, 2], elements[1])
        mesh = {'nodes': nodes, 'elements': elements}

        convert(mesh, define_faces=True)

    def testConvert(self):
        p = MeshParser()
        p.parse('data/pelvis.stl')
        nodes = p.getPoints(pared=True)
        elements = p.getElements(zero_based=False, pared=True)
        mesh = {'nodes': nodes, 'elements': elements}

        convert(mesh, define_faces=True)

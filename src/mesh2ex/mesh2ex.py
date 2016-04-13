def convert(input_mesh=None, output_ex='out.exfile', style_old=False, define_faces=False):
    if input_mesh is None:
        raise ValueError('Value of input mesh is None.')

    if 'nodes' not in input_mesh or 'elements' not in input_mesh:
        raise AttributeError('Input mesh does not have either nodes or elements set.')

    with open(output_ex, 'w') as f:
        f.write('Region: /\n')
        f.write('Shape. Dimension=0\n')
        f.write('#Fields=1\n')
        f.write('1) coordinates, coordinate, rectangular cartesian, #Components=3\n')
        f.write('x. Value index=1, #Derivatives=0\n')
        f.write('y. Value index=2, #Derivatives=0\n')
        f.write('z. Value index=3, #Derivatives=0\n')

        for index, node in enumerate(input_mesh['nodes']):
            f.write('Node: {0}\n'.format(index + 1))
            f.write('{0} {1} {2}\n'.format(node[0], node[1], node[2]))

        elements_faces = {}
        if define_faces:
            faces = []
            for index, el in enumerate(input_mesh['elements']):
                el_a = [el[0]] + [el[0]] + [el[1]]
                el_b = [el[2]] + [el[1]] + [el[2]]
                tmp_faces_for = zip(el_a, el_b)
                tmp_faces_bak = zip(el_b, el_a)
                for i in range(len(tmp_faces_for)):
                    face_f = tmp_faces_for[i]
                    face_b = tmp_faces_bak[i]
                    if face_f not in faces and face_b not in faces:
                        faces.append(face_f)

                    if face_f in faces:
                        face = face_f
                    else:
                        face = face_b

                    if (index + 1) in elements_faces:
                        elements_faces[index + 1].append(faces.index(face) + 1)
                    else:
                        elements_faces[index + 1] = [faces.index(face) + 1]
            f.write('Shape.  Dimension=1 line\n')
            f.write('#Scale factor sets=0\n')
            f.write('#Nodes=0\n')
            f.write('#Fields=0\n')
            for index in range(len(faces)):
                f.write('  Element: 0 0 {0}\n'.format(index + 1))

        f.write('Shape. Dimension=2, simplex(2)*simplex\n')
        f.write('#Scale factor sets=0\n')
        f.write('#Nodes=3\n')
        f.write('#Fields=1\n')
        f.write(' 1) coordinates, coordinate, rectangular cartesian, #Components=3\n')

        for c in ['x', 'y', 'z']:
            f.write('   {0}. l.simplex(2)*l.simplex, no modify, standard node based.\n'.format(c))
            f.write('   #Nodes=3\n')
            f.write('   1.  #Values=1\n')
            f.write('    Value indices:     1\n')
            f.write('    Scale factor indices:   0\n')
            f.write('   2.  #Values=1\n')
            f.write('    Value indices:     1\n')
            f.write('    Scale factor indices:   0\n')
            f.write('   3.  #Values=1\n')
            f.write('    Value indices:     1\n')
            f.write('    Scale factor indices:   0\n')

        for index, element in enumerate(input_mesh['elements']):

            f.write('Element: {0} 0 0\n'.format(index + 1))
            if define_faces:
                f.write('  Faces:\n')
                for face in elements_faces[index + 1]:
                    f.write('    0 0 {0}\n'.format(face))
            f.write('  Nodes:\n')
            for el in element:
                f.write('  {0}'.format(el))
            f.write('\n')

        f.write('\n')
        f.write('\n')

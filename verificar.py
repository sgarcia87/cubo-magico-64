#!/usr/bin/env python3
"""Auditoría reproducible del Cubo 64, sin dependencias externas.

Las operaciones en GF(4) se codifican como XOR y las tablas de
multiplicación por 2 y 3. No modifica ficheros ni hace peticiones de red.
"""
from itertools import product, combinations
from math import dist
M2 = (0, 2, 3, 1)
M3 = (0, 3, 1, 2)


def f(x, y, z):
    u = x ^ M2[y] ^ M3[z]
    v = x ^ M3[y] ^ M2[z]
    return 1 + 2 * (4 * u + v)


def lines():
    out = []
    for a, b in product(range(4), repeat=2):
        out.extend([
            [(t,a,b) for t in range(4)],
            [(a,t,b) for t in range(4)],
            [(a,b,t) for t in range(4)],
        ])
    for axis, fixed in product(range(3), range(4)):
        for inverted in (False, True):
            line = []
            for t in range(4):
                c = [t,3-t if inverted else t]
                c.insert(axis, fixed)
                line.append(tuple(c))
            out.append(line)
    for invert_y, invert_z in product((False,True),repeat=2):
        out.append([(t,3-t if invert_y else t,3-t if invert_z else t) for t in range(4)])
    return out


def run():
    coords = list(product(range(4), repeat=3))
    assert len(coords) == 64
    vals = [f(*p) for p in coords]
    assert set(vals) == set(range(1,32,2))
    assert all(vals.count(v) == 4 for v in range(1,32,2))

    planes = 0
    for axis in range(3):
        for fixed in range(4):
            a = []
            for j in range(4):
                row=[]
                for i in range(4):
                    p=[i,j]
                    p.insert(axis, fixed)
                    row.append(f(*p))
                a.append(row)
            assert sorted(v for row in a for v in row) == list(range(1,32,2))
            sums = [sum(row) for row in a]
            sums += [sum(a[j][i] for j in range(4)) for i in range(4)]
            sums += [sum(a[i][i] for i in range(4)),sum(a[i][3-i] for i in range(4))]
            assert all(v == 64 for v in sums)
            planes += 1

    L = lines()
    assert len(L) == 76
    magic = [sum(f(*p) for p in line)==64 for line in L]
    assert sum(magic) == 72
    diagonal_sums = sorted(sum(f(*p) for p in line) for line in L[-4:])
    assert diagonal_sums == [4,52,76,124]

    assert all(f(x,y,z) == f(3-x,3-y,3-z) for x,y,z in coords)
    assert all(f(t,t,t) == 1 for t in range(4))
    for x,y,z in product((0,3),repeat=3):
        q=(1 if x==0 else 2,1 if y==0 else 2,1 if z==0 else 2)
        assert f(x,y,z)==f(*q)

    tetra = [
        [(3,0,0),(0,3,0),(0,0,3),(3,3,3)],
        [(0,3,3),(3,0,3),(3,3,0),(0,0,0)],
    ]
    for vertices in tetra:
        assert sum(f(*p) for p in vertices) == 64
        assert all(sum((a-b)**2 for a,b in zip(p,q)) == 18 for p,q in combinations(vertices,2))
        assert tuple(sum(p[axis] for p in vertices) / 4 for axis in range(3))==(1.5,1.5,1.5)

    # Las proyecciones normalizadas sobre parejas de ejes son uniformes.
    assert sum(vals) == 1024
    for hidden in range(3):
        for a,b in product(range(4), repeat=2):
            total=0
            for t in range(4):
                p=[a,b]; p.insert(hidden,t)
                total+=f(*p)
            assert total==64

    print('✓ 64 posiciones, 16 impares repetidos 4 veces')
    print(f'✓ {planes}/12 planos mágicos (filas, columnas y diagonales)')
    print(f'✓ {sum(magic)}/76 líneas mágicas; diagonales espaciales {diagonal_sums}')
    print('✓ Simetría central y ocho correspondencias exterior/núcleo')
    print('✓ Dos tetraedros regulares: suma 64, lado 3√2, centroide (1,5; 1,5; 1,5)')
    print('✓ Tres proyecciones bidimensionales uniformes')

if __name__ == '__main__':
    run()

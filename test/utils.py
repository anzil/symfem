"""Utility functions for testing."""

import typing

test_elements: typing.Dict[str, typing.Dict[
    str,
    typing.List[typing.Tuple[typing.Dict[str, typing.Any], typing.Iterable]]
]] = {
    "interval": {
        "P": [({"variant": "equispaced"}, range(6)), ({"variant": "lobatto"}, range(4)),
              ({"variant": "legendre"}, range(5))],
        "vP": [({"variant": "equispaced"}, range(6)), ({"variant": "lobatto"}, range(3)),
               ({"variant": "radau"}, range(3)), ({"variant": "legendre"}, range(3))],
        "dPc": [({"variant": "equispaced"}, range(6)), ({"variant": "lobatto"}, range(4))],
        "bubble": [({"variant": "equispaced"}, range(2, 6)),
                   ({"variant": "lobatto"}, range(2, 3))],
        "serendipity": [({"variant": "equispaced"}, range(1, 6)),
                        ({"variant": "lobatto"}, range(1, 3))],
        "Hermite": [({}, [3])],
        "Bernstein": [({}, range(1, 4))],
        "Taylor": [({}, range(0, 5))],
        "Wu-Xu": [({}, [2])],
        "MWX": [({}, [1])],
        "EG": [({}, range(1, 5))],
    },
    "triangle": {
        "P": [({"variant": "equispaced"}, range(5))],
        "vP": [({"variant": "equispaced"}, range(5))],
        "matrix Lagrange": [({"variant": "equispaced"}, range(3))],
        "symmetric matrix Lagrange": [
            ({"variant": "equispaced"}, range(3))],
        "bubble": [({"variant": "equispaced"}, range(3, 5))],
        "bubble enriched Lagrange": [({"variant": "equispaced"}, range(1, 3))],
        "bubble enriched vector Lagrange":
            [({"variant": "equispaced"}, range(1, 3))],
        "CR": [({"variant": "equispaced"}, [1, 3, 5])],
        "conforming CR": [({}, range(1, 6))],
        "HHJ": [({"variant": "equispaced"}, range(3))],
        "Bell": [({"variant": "equispaced"}, [5])],
        "Morley": [({}, [2])],
        "MWX": [({}, [1, 2])],
        "Regge": [({"variant": "point"}, range(4)), ({"variant": "integral"}, range(3))],
        "AW": [({"variant": "equispaced"}, range(3, 5))],
        "nonconforming AW": [({"variant": "equispaced"}, [2])],
        "Nedelec1": [({"variant": "equispaced"}, range(1, 4))],
        "Nedelec2": [({"variant": "equispaced"}, range(1, 4))],
        "RT": [({"variant": "equispaced"}, range(1, 4))],
        "BDFM": [({"variant": "equispaced"}, range(1, 4))],
        "Argyris": [({}, [5])],
        "MTW": [({"variant": "equispaced"}, [3])],
        "KMV": [({}, [1, 3])],
        "Hermite": [({}, [3])],
        "BDM": [({"variant": "equispaced"}, range(1, 4))],
        "Bernstein": [({}, range(1, 4))],
        "HCT": [({}, [3])],
        "rHCT": [({}, [3])],
        "FS": [({}, [2])],
        "Taylor": [({}, range(0, 5))],
        "Bernardi-Raugel": [({}, [1])],
        "Guzman-Neilan": [({}, [1])],
        "Wu-Xu": [({}, [3])],
        "transition": [({"edge_orders": [1, 1, 1], "variant": "equispaced"}, range(1, 6)),
                       ({"edge_orders": [2, 2, 1], "variant": "equispaced"}, range(1, 6)),
                       ({"edge_orders": [3, 3, 1], "variant": "equispaced"}, range(1, 6)),
                       ({"edge_orders": [3, 3, 2], "variant": "equispaced"}, range(1, 6))],
        "P1-iso-P2": [({}, [1])],
        "EG": [({}, range(1, 4))],
        "LFEG": [({}, range(1, 4))],
        "Alfeld-Sorokina": [({}, [2])],
        "P1 macro": [({}, [1])],
    },
    "tetrahedron": {
        "P": [({"variant": "equispaced"}, range(3))],
        "vP": [({"variant": "equispaced"}, range(3))],
        "matrix Lagrange": [({"variant": "equispaced"}, range(2))],
        "symmetric matrix Lagrange": [({"variant": "equispaced"}, range(2))],
        "bubble": [({"variant": "equispaced"}, [4])],
        "CR": [({"variant": "equispaced"}, [1])],
        "Regge": [({"variant": "point"}, range(3)), ({"variant": "integral"}, range(2))],
        "Nedelec1": [({"variant": "equispaced"}, range(1, 3))],
        "Nedelec2": [({"variant": "equispaced"}, range(1, 3))],
        "RT": [({"variant": "equispaced"}, range(1, 3))],
        "BDFM": [({"variant": "equispaced"}, range(1, 3))],
        "MTW": [({"variant": "equispaced"}, [3])],
        "MWX": [({}, [1, 2, 3])],
        "KMV": [({}, [1])],
        "Hermite": [({}, [3])],
        "BDM": [({"variant": "equispaced"}, range(1, 3))],
        "Bernstein": [({}, range(1, 3))],
        "Taylor": [({}, range(0, 5))],
        "Bernardi-Raugel": [({}, [1, 2])],
        "Guzman-Neilan": [({}, [1, 2])],
        "Wu-Xu": [({}, [4])],
        "transition": [({"edge_orders": [1, 1, 1, 1, 1, 1], "face_orders": [1, 1, 1, 1],
                         "variant": "equispaced"}, range(1, 5)),
                       ({"edge_orders": [1, 1, 1, 1, 1, 1], "face_orders": [3, 3, 1, 1],
                         "variant": "equispaced"}, range(1, 5)),
                       ({"edge_orders": [1, 1, 1, 1, 1, 1], "face_orders": [3, 3, 4, 2],
                         "variant": "equispaced"}, range(1, 5)),
                       ({"edge_orders": [1, 1, 1, 1, 1, 1], "face_orders": [4, 4, 1, 1],
                         "variant": "equispaced"}, range(1, 5)),
                       ({"edge_orders": [2, 2, 2, 2, 2, 2], "face_orders": [1, 1, 1, 1],
                         "variant": "equispaced"}, range(1, 5)),
                       ({"edge_orders": [3, 2, 1, 2, 1, 1], "face_orders": [1, 1, 1, 1],
                         "variant": "equispaced"}, range(1, 5)),
                       ({"edge_orders": [1, 1, 3, 1, 3, 1], "face_orders": [1, 1, 1, 1],
                         "variant": "equispaced"}, range(1, 5)),
                       ({"edge_orders": [1, 1, 2, 1, 2, 5], "face_orders": [3, 3, 2, 5],
                         "variant": "equispaced"}, range(1, 5))],
        "EG": [({}, range(1, 3))],
        "LFEG": [({}, range(1, 3))],
    },
    "quadrilateral": {
        "bubble": [({"variant": "equispaced"}, range(2, 4)), ({"variant": "lobatto"}, range(2, 4))],
        "Q": [({"variant": "equispaced"}, range(4)), ({"variant": "lobatto"}, range(3))],
        "vQ": [({"variant": "equispaced"}, range(4)), ({"variant": "lobatto"}, range(3))],
        "dPc": [({"variant": "equispaced"}, range(4)), ({"variant": "lobatto"}, range(3))],
        "vector dPc": [({"variant": "equispaced"}, range(4)), ({"variant": "lobatto"}, range(3))],
        "serendipity": [({"variant": "equispaced"}, range(1, 4)),
                        ({"variant": "lobatto"}, range(1, 3))],
        "direct serendipity": [({}, range(1, 7))],
        "Scurl": [({"variant": "equispaced"}, range(1, 4)), ({"variant": "lobatto"}, range(1, 3))],
        "Sdiv": [({"variant": "equispaced"}, range(1, 4)), ({"variant": "lobatto"}, range(1, 3))],
        "Qcurl": [({"variant": "equispaced"}, range(1, 4))],
        "Qdiv": [({"variant": "equispaced"}, range(1, 4))],
        "BFS": [({}, [3])],
        "BDFM": [({"variant": "equispaced"}, range(1, 4))],
        "TScurl": [({"variant": "equispaced"}, range(1, 5))],
        "TSdiv": [({"variant": "equispaced"}, range(1, 5))],
        "TNT": [({"variant": "equispaced"}, range(1, 4))],
        "TNTcurl": [({"variant": "equispaced"}, range(1, 4))],
        "TNTdiv": [({"variant": "equispaced"}, range(1, 4))],
        "Regge": [({"variant": "integral"}, range(3))],
        "ABF": [({}, range(3))],
        "AC": [({}, range(4))],
        "Rannacher-Turek": [({}, [1])],
        "P1-iso-P2": [({}, [1])],
        "HZ": [({}, [2, 3, 4])],
        "EG": [({}, range(1, 4))],
        "LFEG": [({}, range(1, 4))],
    },
    "hexahedron": {
        "bubble": [({"variant": "equispaced"}, range(2, 4)), ({"variant": "lobatto"}, range(2, 4))],
        "Q": [({"variant": "equispaced"}, range(3)), ({"variant": "lobatto"}, range(3))],
        "vQ": [({"variant": "equispaced"}, range(3)), ({"variant": "lobatto"}, range(3))],
        "dPc": [({"variant": "equispaced"}, range(3)), ({"variant": "lobatto"}, range(3))],
        "vector dPc": [({"variant": "equispaced"}, range(3)), ({"variant": "lobatto"}, range(3))],
        "serendipity": [({"variant": "equispaced"}, range(1, 3)),
                        ({"variant": "lobatto"}, range(1, 3))],
        "Scurl": [({"variant": "equispaced"}, range(1, 3)), ({"variant": "lobatto"}, range(1, 3))],
        "Sdiv": [({"variant": "equispaced"}, range(1, 3)), ({"variant": "lobatto"}, range(1, 3))],
        "Qcurl": [({"variant": "equispaced"}, range(1, 3))],
        "Qdiv": [({"variant": "equispaced"}, range(1, 3))],
        "BDFM": [({"variant": "equispaced"}, range(1, 3))],
        "BDDF": [({"variant": "equispaced"}, range(1, 3))],
        "TScurl": [({"variant": "equispaced"}, range(1, 4))],
        "TSdiv": [({"variant": "equispaced"}, range(1, 4))],
        "TNT": [({"variant": "equispaced"}, range(1, 2))],
        "TNTcurl": [({"variant": "equispaced"}, range(1, 2))],
        "TNTdiv": [({"variant": "equispaced"}, range(1, 2))],
        "Regge": [({"variant": "integral"}, range(2))],
        "Rannacher-Turek": [({}, [1])],
        "EG": [({}, range(1, 3))],
        "LFEG": [({}, range(1, 3))],
    },
    "prism": {
        "Lagrange": [({"variant": "equispaced"}, range(4))],
        "Nedelec": [({"variant": "equispaced"}, range(1, 3))],
    },
    "pyramid": {
        "Lagrange": [({"variant": "equispaced"}, range(4))],
    }
}

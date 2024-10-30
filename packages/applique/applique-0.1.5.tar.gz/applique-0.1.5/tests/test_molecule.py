"""
Unittests to test molecule object
"""

import unittest
from rdkit import Chem
from rdkit.Chem import (
    rdDepictor,
)  # otherwise it gives import errors during the tests. Strange

import applique as ap
from applique.molecule import Molecule as Mol


class TestMolecule(unittest.TestCase):

    mol_file_benzene = "tests/molecules/benzene.mol"
    mol_file_cyclohexane = "tests/molecules/cyclohexane.mol"
    benzene = Mol()
    benzene = benzene.from_mol(mol_file_benzene)
    cyclohexane = Mol().from_mol(mol_file_cyclohexane)

    def test_from_mol(self):

        assert type(self.benzene.rdmol) == type(
            Chem.rdmolfiles.MolFromMolFile(self.mol_file_benzene)
        )

    def test_struct2D(self):

        ref_benzene = [
            [1.5000000000000004, 7.401486830834377e-17, 0.0],
            [0.7499999999999993, -1.2990381056766587, 0.0],
            [-0.7500000000000006, -1.2990381056766578, 0.0],
            [-1.5, 2.5771188818044677e-16, 0.0],
            [-0.7499999999999996, 1.2990381056766582, 0.0],
            [0.7500000000000006, 1.299038105676658, 0.0],
            [3.0, 2.9605947323337506e-16, 0.0],
            [1.4999999999999996, -2.598076211353318, 0.0],
            [-1.5000000000000007, -2.598076211353315, 0.0],
            [-3.0, 2.9605947323337506e-16, 0.0],
            [-1.4999999999999998, 2.598076211353316, 0.0],
            [1.5000000000000007, 2.598076211353316, 0.0],
        ]

        # case 1
        coordinates = self.benzene.struct2D(self.benzene.rdmol)
        assert coordinates == ref_benzene

        # case 2
        coordinates = self.benzene.struct2D()

        assert coordinates == ref_benzene

    def test_struct3D(self):

        benzene = Mol().from_mol(self.mol_file_benzene)
        cyclohexane = Mol().from_mol(self.mol_file_cyclohexane)

        # case 1
        coordinates = benzene.struct3D(benzene.rdmol)
        assert len(coordinates) == 12

        # case 2
        coordinates_benzene2 = benzene.struct3D()
        assert len(coordinates) == 12

        # case 3
        coordinates = cyclohexane.struct3D()
        assert coordinates != coordinates_benzene2

    def test_sdfile(self):

        sdfile = "tests/molecules/benzene.sdf"
        benzene = Mol().from_sdf(sdfile)

        coordinates = benzene.struct3D()
        assert len(coordinates) == 12

    def test_atomic_number_list(self):
        atom_numbers = self.benzene.get_atom_numbers()
        assert atom_numbers == [6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1]

    def test_atomic_symbols_list(self):
        atom_symbols = self.benzene.get_atom_symbols()
        assert atom_symbols == [
            "C",
            "C",
            "C",
            "C",
            "C",
            "C",
            "H",
            "H",
            "H",
            "H",
            "H",
            "H",
        ]

    def test_from_xyz_block(self):

        xyz_block="""3

O      0.000000    0.000000    0.117790
H      0.000000    0.755450   -0.471160
H      0.000000   -0.755450   -0.471160
"""
        mol = Mol().from_xyz_block(xyz_block)
        coords = mol.struct3D(embed=False)
        assert coords == [[0.0, 0.0, 0.11779], [0.0, 0.75545, -0.47116], [0.0, -0.75545, -0.47116]]
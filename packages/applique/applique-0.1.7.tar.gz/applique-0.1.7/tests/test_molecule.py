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

    def test_get_2D_coordinates(self):

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
        coordinates = self.benzene.get_2D_coordinates(self.benzene.rdmol)
        assert coordinates == ref_benzene

        # case 2
        coordinates = self.benzene.get_2D_coordinates()

        assert coordinates == ref_benzene

    def test_get_3D_coordinates(self):

        benzene = Mol().from_mol(self.mol_file_benzene)
        cyclohexane = Mol().from_mol(self.mol_file_cyclohexane)

        # case 1
        coordinates = benzene.get_3D_coordinates(benzene.rdmol)
        assert len(coordinates) == 12

        # case 2
        coordinates_benzene2 = benzene.get_3D_coordinates()
        assert len(coordinates) == 12

        # case 3
        coordinates = cyclohexane.get_3D_coordinates()
        assert coordinates != coordinates_benzene2

    def test_sdfile(self):

        sdfile = "tests/molecules/benzene.sdf"
        benzene = Mol().from_sdf(sdfile)

        coordinates = benzene.get_3D_coordinates()
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
    
    def test_from_xyz_file(self): 
        
        mol = Mol().from_xyz_file("tests/molecules/benzene.xyz")
        coords = mol.get_3D_coordinates(embed=False) #because bonds not relevant
        assert coords == [[-0.244413, 1.373238, -0.00442], [-1.311251, 0.474916, -0.0248], [-1.066838, -0.898322, -0.020383], [0.244413, -1.373238, 0.004417], [1.311251, -0.474916, 0.024803], [1.066838, 0.898322, 0.020383], [-0.434839, 2.443148, -0.007866], [-2.332866, 0.844931, -0.04412], [-1.898027, -1.598218, -0.036262], [0.434839, -2.443148, 0.007856], [2.332866, -0.844931, 0.044129], [1.898027, 1.598217, 0.036264]]

    def test_from_xyz_block(self):

        xyz_block = """3

O      0.000000    0.000000    0.117790
H      0.000000    0.755450   -0.471160
H      0.000000   -0.755450   -0.471160
"""
        mol = Mol().from_xyz_block(xyz_block)
        coords = mol.get_3D_coordinates(embed=False)
        assert coords == [
            [0.0, 0.0, 0.11779],
            [0.0, 0.75545, -0.47116],
            [0.0, -0.75545, -0.47116],
        ]

    def test_get_xyz_block(self):

        xyz_block = self.benzene.get_xyz_block()
        assert (
            xyz_block
            == "12\n\nC      -1.0879842700272027    0.872416451534302    -0.026825355553469633\nC      -1.2998219370699033    -0.5059644835578699    0.00017864384975932324\nC      -0.21183783816609797    -1.3783804365854642    0.027003738629617618\nC      1.0879846928171655    -0.8724159895862993    0.0268279140019364\nC      1.2998230865381217    0.5059651197107923    -0.0001784526055434865\nC      0.21183827551073217    1.3783816707549486    -0.027002375253142707\nH      -1.935649989181456    1.5521282747053937    -0.04772734399363389\nH      -2.3125328916373658    -0.9001706015914183    0.00032112279332168554\nH      -0.3768855513108287    -2.4522978070714867    0.048039089305949266\nH      1.9356489971010447    -1.552129581990307    0.04773047568214471\nH      2.312535702047898    0.9001675642755037    -0.00032409210453793424\nH      0.3768817233779219    2.4522998194018983    -0.04804336475240809"
        )

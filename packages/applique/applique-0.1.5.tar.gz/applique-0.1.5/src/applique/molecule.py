from typing import List
import rdkit
from rdkit.Chem import AllChem


class Molecule:
    """
    Simple molecule class that extends RDKit molecules
    """

    def from_canonical_smiles(self, can_smiles: str) -> None:
        raise NotImplementedError

    def from_mol(self, file_path: str) -> None:
        self.rdmol = rdkit.Chem.rdmolfiles.MolFromMolFile(file_path)
        return self

    def from_xyz_block(self, xyz_block:str)-> None: 
        self.rdmol = rdkit.Chem.rdmolfiles.MolFromXYZBlock(xyz_block)
        return self

    def from_sdf(self, file_path: str) -> None:
        """
        It is a bit hacky to admit. Becasuse SDF files usually store more molecules,
        only the first molecule of the whole collection is selected.

        """
        supplier = rdkit.Chem.rdmolfiles.SDMolSupplier(file_path)
        mol = supplier[0]
        self.rdmol = mol
        return self

    def get_atom_numbers(self, rdmol=None):
        """
        Useful for generating graphs and xyz_files
        """

        mol = self.embed(rdmol=rdmol)

        atomic_numbers = []
        for atom in mol.GetAtoms():
            atomic_numbers.append(atom.GetAtomicNum())
        return atomic_numbers

    def get_atom_symbols(self, rdmol=None):
        """
        Is useful for creating your own xyz files
        """

        mol = self.embed(rdmol=rdmol)
        atomic_symbols = []

        for atom in mol.GetAtoms():
            atomic_symbols.append(atom.GetSymbol())
        return atomic_symbols

    def embed(self, rdmol=None):
        """make emebedding in RDKit0:00 • 58.8 MB/s


        Args:
            rdmol (_type_, optional): rdmol object. Defaults to None.

        Returns:
            _type_: Mol Object
        """
        mol = self._check_mol(rdmol=rdmol)
        mol = rdkit.Chem.rdmolops.AddHs(mol)
        assert type(mol) != None
        AllChem.EmbedMolecule(mol)
        AllChem.MMFFOptimizeMolecule(mol)
        self.rdmol = mol
        return mol

    def struct2D(self, rdmol=None, embed=True) -> List[float]:
        """Gets 2D coordinates

        Args:
            rdmol (_type_, optional): RDMol object

        Returns:
            List[float]: Coordinates 3D but only in 2D
        """
        if embed == True: 
            mol = self.embed(rdmol=rdmol)
        else: 
            if rdmol is None: 
                rdmol = self.rdmol
            mol = rdmol

        rdkit.Chem.rdDepictor.Compute2DCoords(mol)
        coordinates = []

        for i in range(len(mol.GetAtoms())):
            pos = mol.GetConformer().GetAtomPosition(i)
            coordinates.append(list(pos))
        self.coordinates2D = coordinates

        return coordinates

    def struct3D(self, rdmol=None, embed=True) -> List[List[float]]:
        """Gets 2D coordinates

        Args:
            rdmol (_type_, optional): RDMol object

        Returns:
            List[float]: Coordinates 3D but only in 2D
        """

        if embed == True: 
            mol = self.embed(rdmol=rdmol)
        else: 
            if rdmol is None: 
                rdmol = self.rdmol
            mol = rdmol


        coordinates = []

        for i in range(len(mol.GetAtoms())):
            pos = mol.GetConformer().GetAtomPosition(i)
            coordinates.append(list(pos))
        self.coordinates3D = coordinates

        return coordinates

    def _check_mol(self, rdmol):
        """
        Reused snipptet to either use the stored rdmol or a new one
        """

        if rdmol is None:
            mol = self.rdmol
        else:
            mol = rdmol
        return mol


class MoleculeCollection:
    """
    Defines a collection of molecules, for example for solvent or gas phase mixtures
    """

    def __init__(self, molecules, Box):

        self.molecules = molecules
        self.Box = Box

    def add_molecules(self, molecules) -> None:

        assert type(molecules) == type([])
        self.molecules.append(molecules)

    def remove_molecules(self, indices: List) -> None:

        assert type(indices) == type([])
    
    def get_atoms_from_molecule(self, Molecule)->List[List[str | float]]: 

        atom_numbers = Molecule.get_atom_numbers()
        atom_symbols = Molecule.get_atom_symbols
        return [atom_numbers, atom_symbols]


class MoleculeCollectionIndistinct:
    """
    Defines a molecular collection with indistinct molecules. That means only atom positions are relevant

    """

    def __init__(self):
        pass

    def add_molecules(self):
        # need to unpack the atom coordinates
        raise NotImplementedError

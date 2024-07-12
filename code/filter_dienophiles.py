import pandas as pd
from rdkit import Chem

def checkForDiene(x):
    patterns = [
        '[$(C=CC=C)]',
        '[$(C=CC=N)]',
        '[$(C=CN=N)]',
        '[$(C=NC=N)]',
        '[$(C=NN=N)]',
        '[$(N=CN=N)]',
        '[$(N=NN=N)]',
        '[$(N=CC=N)]',
        '[$(C=NN=C)]',
        '[$(C=CC=O)]',
        '[$(O=CC=O)]',
        '[$(C=CC=O)]',
        '[$(C=CN=O)]',
        '[$(C=NC=O)]',
        '[$(C=NN=O)]',
        '[$(N=NN=O)]',
        '[$(N=CC=O)]',
        '[$(N=NC=O)]',
        '[$(N=CN=O)]',
        '[$(O=NN=O)]',
        '[$(O=CN=O)]',
        '[$(O=NC=O)]',
    ]

    m = Chem.MolFromSmiles(x)
    if m is not None:
        for p in patterns:
            patt = Chem.MolFromSmarts(p)

            if m.HasSubstructMatch(patt):
                return True
    else:
        return False

def checkForAlkene(x):
    patterns = [
        'C=C',
    ]

    m = Chem.MolFromSmiles(x)
    if m is not None:
        for p in patterns:
            patt = Chem.MolFromSmarts(p)

            if m.HasSubstructMatch(patt):
                return True
    else:
        return False

def checkForCNOS(x):

    pattern = [6,7,8,16]

    m = Chem.MolFromSmiles(x)

    for atom in m.GetAtoms():
        if atom.GetAtomicNum() not in pattern:
            return False
    
    return True

if __name__ == '__main__':
    data = pd.read_csv('/home/michiel/Paper-Electrophilic-AI/datasets/gdb13/10.smi', sep='\t', names=['smiles'])

    data = data[['smiles']]

    data['dienophile'] = data['smiles'].apply(lambda x: checkForAlkene(x))
    data['cnos'] = data['smiles'].apply(lambda x: checkForCNOS(x))
    
    data = data.loc[data['dienophile'] == True]
    data = data.loc[data['cnos'] == True]
    data = data[['smiles']]

    data.to_csv('datasets/gdb13_10ha_cnos_dienophiles.csv', index=False)

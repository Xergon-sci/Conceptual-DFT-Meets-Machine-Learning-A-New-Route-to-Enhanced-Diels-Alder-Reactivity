# Conceptual DFT Meets Machine Learning: A New Route to Enhanced Diels-Alder Reactivity

DOI: tba

This repository contains the code, data, and scripts associated with the forthcoming manuscript _“Conceptual DFT Meets Machine Learning: A New Route to Enhanced Diels–Alder Reactivity”_.

## Installation
Clone the repository with:

```git clone https://github.com/Xergon-sci/Conceptual-DFT-Meets-Machine-Learning-A-New-Route-to-Enhanced-Diels-Alder-Reactivity.git```

From the repository folder, install the dependencies with your preferred virtual environment manager from requirements.txt:

```pip install -r requirements.txt```

## Usage
To use the model via python you need to build the predictor and call predict() while passing a list ot numpy array of SMILES.
```python

# Set up the validator
val = MJ1_Validator(input='smiles')

# Set up the preprocessor
prep = MJ1_Preprocessor(optimize=True)

# Load the model and assign validators and preprocessors
pred = MJ1_Predictor(
    model_path='models/electrophilicity_index.tf',
    validator=val,
    preprocessor=prep)

# use the predictor
predictions = predictor.predict("C1CCC(CC1)CC(O)O") # or pass a list of SMILES
```
A full exaple can be seen [here](code/predict.py).

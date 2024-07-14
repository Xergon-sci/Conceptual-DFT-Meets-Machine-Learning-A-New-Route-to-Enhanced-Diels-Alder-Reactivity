import os
import pandas as pd
from pandas.core.common import flatten
import tensorflow as tf
from adftPerformance.models.MJ1 import MJ1_Validator, MJ1_Preprocessor, MJ1_Predictor

def initialize_model():
    val = MJ1_Validator(input='smiles')
    prep = MJ1_Preprocessor(optimize=True)

    pred = MJ1_Predictor(
        model_path='models/electrophilicity_index.tf',
        validator=val,
        preprocessor=prep)

    return pred

def main():

    # Initialize the models
    predictor = initialize_model()

    # load the data
    data = pd.read_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_3.csv')

    # make the predictions
    smiles_list = data['smiles'].tolist()
    predictions = predictor.predict(smiles_list)
    predictions = list(flatten(predictions['dense_2']))
    data = data.assign(predicted_w_eV=predictions)

    # save them to file
    data.to_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_predictions_3.csv', index=False)


if __name__ == '__main__':
    main()
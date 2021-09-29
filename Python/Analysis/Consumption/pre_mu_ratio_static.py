#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import params
import pandas as pd
from . import cns_funcs as func


def main(input_folder, output_folder):
    # read csv file
    file = input_folder + 'pre_exp_pc.csv'
    df = pd.read_csv(file)
    PA_gammaA = params.gammaA
    etaA = params.etaA
    etaM = params.etaM

    # Create a column for marginal utility ratio
    df = func.create_mu_ratio_static(df, PA_gammaA, etaA, etaM)

    # Save the dataframe to a csv file
    file_name = 'pre_mu_ratio_static.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    input_folder = '../../Data/Downloads/Pre/'
    output_folder = ''
    main(input_folder, output_folder)

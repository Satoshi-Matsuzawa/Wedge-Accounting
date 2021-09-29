#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import cns_funcs as func


def main(input_folder, output_folder):
    # read csv file
    file_exp = input_folder + 'pre_exp_pc.csv'
    file_CPI = input_folder + 'pre_CPI.csv'
    df_exp = pd.read_csv(file_exp)
    df_CPI = pd.read_csv(file_CPI)
    df = df_exp.merge(df_CPI, on='year_wst').copy()

    # # Create a column for marginal utility ratio
    df = func.create_mu_ratio_dynamic(df)

    # Save the dataframe to a csv file
    file_name = 'pre_mu_ratio_dynamic.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    input_folder = '../../Data/Downloads/Pre/'
    output_folder = ''
    main(input_folder, output_folder)

#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import params
import pandas as pd
from . import prd_funcs as func


def main(input_folder, output_folder):
    # read csv file
    file_cap = input_folder + 'pre_cap.csv'
    file_GDP = input_folder + 'pre_GDP.csv'
    df_cap = pd.read_csv(file_cap)
    df_GDP = pd.read_csv(file_GDP)
    df = df_cap.merge(df_GDP, on='year_wst').copy()

    alphaKA = params.alphaKA
    alphaKM = params.alphaKM

    df = func.create_cap_prd_ratio(df, alphaKA, alphaKM)
    df = func.create_cap_ratio(df)
    df = func.create_output_ratio(df)

    # Save the dataframe to a csv file
    file_name = 'pre_cap_prd_ratio.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    input_folder = '../../Data/Downloads/Pre/'
    output_folder = ''
    main(input_folder, output_folder)

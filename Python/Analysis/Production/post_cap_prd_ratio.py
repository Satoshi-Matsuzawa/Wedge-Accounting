#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import params
import pandas as pd
from . import prd_funcs as func


def main(input_folder, output_folder):
    # read csv file
    file_cap = input_folder + 'post_cap.csv'
    file_GDP = input_folder + 'post_GDP.csv'
    df_cap = pd.read_csv(file_cap)
    df_GDP = pd.read_csv(file_GDP)

    # divide by 1000 to make the unit common.
    # GDP is in billions of yen
    # Capital is in millions of yen
    denom = 1000

    columns = ['tot_cap', 'prm_cap', 'non_prm_cap']
    for column in columns:
        df_cap[column] = df_cap[column] / denom

    # Change the data type to merge the data frames
    df_cap['year_jpn'] = df_cap['year_jpn'].astype(str)
    df_GDP['year_jpn'] = df_GDP['year_jpn'].astype(str)

    df = df_cap.merge(df_GDP, on='year_jpn').copy()

    alphaKA = params.alphaKA
    alphaKM = params.alphaKM

    df = func.create_cap_prd_ratio(df, alphaKA, alphaKM)
    df = func.create_cap_ratio(df)
    df = func.create_output_ratio(df)

    # Save the dataframe to a csv file
    file_name = 'post_cap_prd_ratio.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    input_folder = '../../Data/Downloads/Post/'
    output_folder = ''
    main(input_folder, output_folder)

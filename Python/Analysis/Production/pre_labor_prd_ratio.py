#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import params
import pandas as pd
from . import prd_funcs as func


def main(input_folder, output_folder):
    # read csv file
    file_emp = input_folder + 'pre_emp.csv'
    file_GDP = input_folder + 'pre_GDP.csv'
    df_emp = pd.read_csv(file_emp)
    df_GDP = pd.read_csv(file_GDP)
    df = df_emp.merge(df_GDP, on='year_wst').copy()

    alphaLA = params.alphaLA
    alphaLM = params.alphaLM

    df = func.create_labor_prd_ratio(df, alphaLA, alphaLM)
    df = func.create_labor_ratio(df)
    df = func.create_output_ratio(df)

    # Save the dataframe to a csv file
    file_name = 'pre_labor_prd_ratio.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    input_folder = '../../Data/Downloads/Pre/'
    output_folder = ''
    main(input_folder, output_folder)

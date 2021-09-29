#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import pre_functions as pre_func


def main(output_folder):
    url = 'https://d-infra.ier.hit-u.ac.jp/Japanese/ltes/LTES_06_01.xlsx'
    xl = pd.ExcelFile(url)

    sheet_name = '第4表'
    df = pre_func.create_cleaned_df(xl, sheet_name)

    # Select Year, food expenditure 'J0604__001',
    # and total consumption expenditure 'J0604__010'.
    df = df.loc[:, ['year_wst', 'J0604__001', 'J0604__010']]

    # Set the column name
    df.columns = ['year_wst', 'food', 'cons']

    # Create a column for non-food consumption
    df['non_food'] = df['cons'] - df['food']

    # Save the dataframe to a csv file
    file_name = 'pre_exp_pc.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded'
    main(output_folder)

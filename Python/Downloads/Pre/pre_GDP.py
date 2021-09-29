#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import pre_functions as pre_func


def main(output_folder):
    url = 'http://d-infra.ier.hit-u.ac.jp/Japanese/ltes/LTES_01.xlsx'
    xl = pd.ExcelFile(url)

    sheet_name = '第25表'
    df = pre_func.create_cleaned_df(xl, sheet_name)

    # Select Year, Agricultural GDP 'J0125__001', and Total GDP 'J0125__006'.
    df = df.loc[:, ['year_wst', 'J0125__001', 'J0125__006']]

    # Set the column name
    df.columns = ['year_wst', 'prm_GDP', 'tot_GDP']

    # Create a column for non-primary GDP
    df['non_prm_GDP'] = df['tot_GDP'] - df['prm_GDP']

    # Save the dataframe to a csv file
    file_name = 'pre_GDP.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded'
    main(output_folder)

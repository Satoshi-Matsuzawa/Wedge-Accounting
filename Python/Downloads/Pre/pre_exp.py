#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import pre_functions as pre_func


def main(output_folder):
    url = 'http://d-infra.ier.hit-u.ac.jp/Japanese/ltes/LTES_01.xlsx'
    xl = pd.ExcelFile(url)

    sheet_name = '第19表'
    df = pre_func.create_cleaned_df(xl, sheet_name)

    # Select Year, food expenditure 'J0125__001',
    # and total consumption expenditure 'J0125__011'.
    df = df.loc[:, ['year_wst', 'J0119__001', 'J0119__011']]

    # Set the column name
    df.columns = ['year_wst', 'food', 'cons']

    # Divide food spending by 1000 so that both food spending
    # and total consumer spending are in units of 1 million yen.
    df['food'] = df['food'] / 1000

    # Create a column for non-food consumption
    df['non_food'] = df['cons'] - df['food']

    # Save the dataframe to a csv file
    file_name = 'pre_exp.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded'
    main(output_folder)

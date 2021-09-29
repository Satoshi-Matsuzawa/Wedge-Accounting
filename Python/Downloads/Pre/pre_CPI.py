#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import pre_functions as pre_func


def main(output_folder):
    url = 'http://d-infra.ier.hit-u.ac.jp/Japanese/ltes/LTES_08.xlsx'
    xl = pd.ExcelFile(url)

    # df1 is for CPI
    # In the note in Table 1, the authors of the statistics state that
    # the prewar CPI does not include the primary industry.
    # J0801__002 in Table 1 is the same as J0802__001 in Table 2,
    # but the latter has one more digit.
    sheet_name1 = '第2表'
    df1 = pre_func.create_cleaned_df(xl, sheet_name1)

    # df2 is for price index for agricultural products
    sheet_name2 = '第10表'
    df2 = pre_func.create_cleaned_df(xl, sheet_name2)

    # df3 is for price index for industrial products
    sheet_name3 = '第15表'
    df3 = pre_func.create_cleaned_df(xl, sheet_name3)

    # Select columns for df1
    # CPI, 1934-36 = 100, 'J0802__001'
    # CPI: Urban Families: Food, 'J0802__005'
    # CPI: Urban Families: Clothing, 'J0802__006'
    df1 = df1[['year_wst', 'J0802__001', 'J0802__005', 'J0802__006']]

    # Select columns for df2
    # Agricultural product price index, 1934-36 = 100, 'J0810__004'
    # J0810__004 has two rows, one for pre-war and one for post-war.
    # Use prewar column.
    df2 = df2[['year_wst', 'J0810__004_1']]

    # Select columns for df3
    # Price Indexes of Manufacturfing and Mining Products, 'J0815__001'
    # J0815__001 has two rows, one for pre-war and one for post-war.
    # Use prewar column.
    df3 = df3[['year_wst', 'J0815__001_1']]

    # Set the column name
    df1.columns = ['year_wst', 'cpi_goods', 'cpi_agr', 'cpi_ind']
    df2.columns = ['year_wst', 'ppi_agr']
    df3.columns = ['year_wst', 'ppi_ind']

    # Merge data frames
    df = pd.merge(pd.merge(df1, df2, on='year_wst'), df3, on='year_wst')

    # Save the dataframe to a csv file
    file_name = 'pre_CPI.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded/'
    main(output_folder)

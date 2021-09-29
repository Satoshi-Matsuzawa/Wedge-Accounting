#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import post_functions as post_func


def main(output_folder):
    # Download data prior to 1962
    url1 = 'https://warp.da.ndl.go.jp/info:ndljp/pid/11423429/www.stat.go.jp/data/chouki/zuhyou/20-01-a.xls'
    df1 = pd.read_excel(url1, header=None, index_col=None)
    df1 = post_func.drop_empty_columns_and_rows(df1)

    # Download data after 1963
    url2 = 'https://warp.da.ndl.go.jp/info:ndljp/pid/11423429/www.stat.go.jp/data/chouki/zuhyou/20-01-b.xls'
    df2 = pd.read_excel(url2, header=None, index_col=None)
    df2 = post_func.drop_empty_columns_and_rows(df2)

    # Select the year of the Japanese calendar, that of the Western calendar,
    # household size, consumption expenditure, and food expenditure.
    df1 = df1.iloc[6:, [0, 1, 3, 5, 6]]
    df2 = df2.iloc[5:50, [0, 1, 4, 7, 8]]

    # Set the column name
    columns = ['year_jpn', 'year_wst', 'hh_size', 'cons', 'food']
    df1.columns = columns
    df2.columns = columns

    # Concatenate data frames
    df = pd.concat([df1, df2])

    # Clean the column of the Japanese calendar year
    post_func.clean_year(df, 'year_jpn')

    # Create a column for non-food consumption
    df['non_food'] = df['cons'].astype(int) - df['food'].astype(int)

    # Create per capita variables
    df['cons_pc'] = df['cons'] / df['hh_size']
    df['food_pc'] = df['food'] / df['hh_size']
    df['non_food_pc'] = df['non_food'] / df['hh_size']

    # Save the dataframe to a csv file
    file_name = 'post_exp.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded/'
    main(output_folder)

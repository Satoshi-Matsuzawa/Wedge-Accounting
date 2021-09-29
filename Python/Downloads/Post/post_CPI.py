#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import post_functions as post_func


def main(output_folder):
    url = 'https://warp.da.ndl.go.jp/info:ndljp/pid/11423429/www.stat.go.jp/data/chouki/zuhyou/22-14.xls'
    df = pd.read_excel(url, header=None, index_col=None)
    df = post_func.drop_empty_columns_and_rows(df)

    # Select the year of the Japanese calendar, that of the Western calendar,
    # the price index of goods, agricultural and fishery products,
    # and industrial products.
    # Select a series starting in 1955.
    df = df.loc[11:66, [0, 1, 3, 5, 9]]

    # Set the column name
    df.columns = ['year_jpn', 'year_wst', 'cpi_goods', 'cpi_agr', 'cpi_ind']

    # Clean the year column
    post_func.clean_year(df, 'year_wst')

    # Clean the column of the Japanese calendar year
    post_func.clean_year(df, 'year_jpn')

    # Save the dataframe to a csv file
    file_name = 'post_CPI.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded/'
    main(output_folder)

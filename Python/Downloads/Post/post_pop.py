#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import post_functions as post_func


def main(output_folder):
    url = 'https://warp.da.ndl.go.jp/info:ndljp/pid/11423429/www.stat.go.jp/data/chouki/zuhyou/02-01.xls'
    df = pd.read_excel(url, header=None, index_col=None)
    df = post_func.drop_empty_columns_and_rows(df)

    # Select the year of the the Western calendar, and the total population
    df = df.iloc[3:, [1, 2]]

    # Set the column name
    df.columns = ['year_wst', 'tot_pop']

    # There is a duplication in the 1970 data
    # Remove duplicates
    df = df.drop([110])

    # Save the dataframe to a csv file
    file_name = 'post_pop.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded/'
    main(output_folder)

#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import post_functions as post_func


def main(output_folder):
    url = "https://warp.da.ndl.go.jp/info:ndljp/pid/11423429/www.stat.go.jp/data/chouki/zuhyou/03-03-a.xls"
    df = pd.read_excel(url, header=None, index_col=None)
    df = post_func.drop_empty_columns_and_rows(df)

    # Select the year of the Japanese calendar, that of the Western calendar,
    # the total GDP of the private sector, and the GDP of the primary sector.
    df = df.iloc[:, [0, 1, 2, 3, 23]]

    # Set the column name
    df.columns = ['year_jpn', 'year_wst', 'tot_prv_GDP', 'prm_GDP', 'tot_GDP']

    # Remove nominal GDP and GDP deflator
    # Leave only real GDP at 1990 prices
    df = df.loc[55:100, :]

    # Clean the column of the Japanese calendar year
    post_func.clean_year(df, 'year_jpn')

    # Create a column for non-primary GDP
    df['non_prm_GDP'] = df['tot_prv_GDP'] - df['prm_GDP']

    # Save the dataframe to a csv file
    file_name = 'post_GDP.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded/'
    main(output_folder)

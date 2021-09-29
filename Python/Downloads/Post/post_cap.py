#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import post_functions as post_func


def main(output_folder):
    url = 'https://www.esri.cao.go.jp/jp/sna/data/data_list/minkan/files/tables/h7/0911stock.xls'
    sheet_name = 'ストック額(進捗ベース)'
    df = pd.read_excel(url, sheet_name=sheet_name, header=None, index_col=None)
    df = post_func.drop_empty_columns_and_rows(df)

    # Select total capital and primary sector capital
    df = df.iloc[2:, [0, 1, 2]]

    # Set the column name
    df.columns = ['year_quarter', 'tot_cap', 'prm_cap']

    # Select first-quarter data
    df = df.iloc[::4]

    # Create a column of Japanese calendar years
    df['year_jpn'] = df['year_quarter'].astype(str).str[:-6]
    df = df.drop(['year_quarter'], axis=1)
    # df['year_jpn'] = df['year_jpn'].astype(str)

    # Create a column for non-primary sector capital
    df['non_prm_cap'] = df['tot_cap'] - df['prm_cap']

    # Save the dataframe to a csv file
    file_name = 'post_cap.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded/'
    main(output_folder)

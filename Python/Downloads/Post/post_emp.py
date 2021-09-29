#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import post_functions as post_func


def main(output_folder):
    url = "https://warp.da.ndl.go.jp/info:ndljp/pid/11423429/www.stat.go.jp/data/chouki/zuhyou/19-08-a.xls"
    df = pd.read_excel(url, header=None, index_col=None)
    df = post_func.drop_empty_columns_and_rows(df)

    # Select the year and total employment of total
    # the primary, secondary, and tertiary industries
    df = df.iloc[:, [0, 1, 2, 35, 36, 40, 44]]

    # Set the column name
    df.columns = ['year_jpn', 'year_wst', 'tot_emp',
                  'pub_emp', 'prm_emp', 'scn_emp', 'trt_emp']

    # Remove male and female employment
    # Leave only total employment
    df = df.loc[11:61, :]

    # Clean the column of the Japanese calendar year
    post_func.clean_year(df, 'year_jpn')

    # Create a column for non-primary employment
    df['non_prm_emp'] = df['scn_emp'] + df['trt_emp'] - df['pub_emp']

    # Save the dataframe to a csv file
    file_name = 'post_emp.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded/'
    main(output_folder)

#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import pre_functions as pre_func


def main(output_folder):
    url = 'http://d-infra.ier.hit-u.ac.jp/Japanese/ltes/LTES_02.xlsx'
    xl = pd.ExcelFile(url)

    # df1 is for data from 1871 to 1920
    sheet_name1 = '第1表'
    df1 = pre_func.create_cleaned_df(xl, sheet_name1)

    # df2 is for data from 1920 to 1940
    sheet_name2 = '第2表'
    df2 = pre_func.create_cleaned_df(xl, sheet_name2)

    # Select columns for df1
    # Total population of both men and women 'J0201__215'
    df1 = df1[['year_wst', 'J0201__215']]

    # Select columns for df2
    # Total population of both men and women 'J0202__215'
    df2 = df2[['year_wst', 'J0202__215']]

    # The 1920 data is duplicated between the two data frames.
    # Remove it from the second data frame.
    df2 = df2.iloc[1:, ]

    # Set the column name
    columns = ['year_wst', 'tot_pop']
    df1.columns = columns
    df2.columns = columns

    # Concatenate data frames
    df = pd.concat([df1, df2])

    # Save the dataframe to a csv file
    file_name = 'pre_pop.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded/'
    main(output_folder)

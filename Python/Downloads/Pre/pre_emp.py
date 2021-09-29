#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import pre_functions as pre_func


def main(output_folder):
    url = 'http://d-infra.ier.hit-u.ac.jp/Japanese/ltes/LTES_02.xlsx'
    xl = pd.ExcelFile(url)

    # df1 is for data from 1906 to 1920
    sheet_name1 = '第8表'
    df1 = pre_func.create_cleaned_df(xl, sheet_name1)

    # df2 is for data from 1920 to 1940
    sheet_name2 = '第9表'
    df2 = pre_func.create_cleaned_df(xl, sheet_name2)

    # Select columns for df1
    # All industry workers: total of men and women 'J0208__301'
    # Primary industry workers: total of men and women 'J0208__302'
    # Secondary industry workers: total of men and women 'J0208__305'
    # Tertiary industrial workers: total of men and women  'J0208__324'
    # Army and Navy: total of men and women 'J0208__327'
    df1 = df1[['year_wst', 'J0208__301', 'J0208__302',
               'J0208__305', 'J0208__324', 'J0208__327']]

    # Select columns for df2
    # All industry workers: total of men and women 'J0209__301'
    # Primary industry workers: total of men and women 'J0209__302'
    # Secondary industry workers: total of men and women 'J0209__305'
    # Tertiary industrial workers: total of men and women  'J0209__322'
    # Army and Navy: total of men and women 'J0208__331'
    df2 = df2[['year_wst', 'J0209__301', 'J0209__302',
               'J0209__305', 'J0209__322', 'J0209__331']]

    # The 1920 data is duplicated between the two data frames.
    # Remove it from the second data frame.
    df2 = df2.iloc[1:, ]

    # Set the column name
    columns = ['year_wst', 'tot_emp', 'prm_emp', 'scn_emp', 'trt_emp', 'mil']
    df1.columns = columns
    df2.columns = columns

    # Concatenate data frames
    df = pd.concat([df1, df2])

    # Create a column for non-primary employment
    df['non_prm_emp'] = df['scn_emp'] + df['trt_emp'] - df['mil']

    # Save the dataframe to a csv file
    file_name = 'pre_emp.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded/'
    main(output_folder)

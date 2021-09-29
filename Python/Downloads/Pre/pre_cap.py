#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
from . import pre_functions as pre_func


def main(output_folder):
    url = 'http://d-infra.ier.hit-u.ac.jp/Japanese/ltes/LTES_03_02.xlsx'
    xl = pd.ExcelFile(url)

    # df1 is for primary industry
    sheet_name1 = '第56表'
    df1 = pre_func.create_cleaned_df(xl, sheet_name1)

    # df2 is for non-primary industry
    sheet_name2 = '第57表'
    df2 = pre_func.create_cleaned_df(xl, sheet_name2)

    # Select columns for df1
    # Total capital stock of primary industry (7-year average) 'J0356__010'
    # Since post-war capital data is also gross total capital stock,
    # we will use gross total capital stock.
    # See https://www.esri.cao.go.jp/jp/sna/data/data_list/minkan/files/contents/pdf/162stock_announce.pdf
    df1 = df1[['year_wst', 'J0356__005']]

    # Select columns for df2
    # Total capital stock of non-primary industry (7-year average) 'J0357__014'
    df2 = df2[['year_wst', 'J0357__007']]

    # Select rows that contains the data
    # The data before 1880 is incomplete and is not used.
    df1 = df1.iloc[3:, ]
    # The second dataset starts in 1878.
    # Remove the 1877 data from the first data set.
    df2 = df2.iloc[3:, ]

    # Set the column name
    df1.columns = ['year_wst', 'prm_cap']
    df2.columns = ['year_wst', 'non_prm_cap']

    # Merge data frames
    df = pd.merge(df1, df2, on='year_wst')

    # Save the dataframe to a csv file
    file_name = 'pre_cap.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded/'
    main(output_folder)

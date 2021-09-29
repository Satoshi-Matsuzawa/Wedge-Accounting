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

    # df3 is for price index for industrial products
    sheet_name4 = '第1表'
    df4 = pre_func.create_cleaned_df(xl, sheet_name4)
    # Create a temporary data frame to get the linked index.
    df4_temp = xl.parse(sheet_name4, header=None, index_col=None)

    # Select columns for df1
    # The seventh column from the end has the year of postwar data
    df1.columns.values[-7] = 'year_wst_post'
    # CPI, 1789-1938, 1934-36 = 100, General, 'J0802__001'
    # CPI, 1789-1938, 1934-36 = 100, Urban Families: Food, 'J0802__005'
    # CPI, 1789-1938, 1934-36 = 100, Urban Families: Clothing, 'J0802__006'
    # CPI, 1946-1965, 1934-36 = 1, General, 'J0802__101'
    # CPI, 1951-1965, 1934-36 = 1, Food, 'J0802__102'
    # CPI, 1951-1965, 1934-36 = 1, Clothing, 'J0802__103'
    df1_pre = df1[['year_wst',
                   'J0802__001', 'J0802__005', 'J0802__006']].copy()
    df1_post = df1[['year_wst_post',
                    'J0802__101', 'J0802__102',  'J0802__103']].copy()
    # Delete empty rows
    df1_post = df1_post.dropna()

    # Multiply the column of df1_post by 100
    # so that 1934-1936 = 100 in both data frames.
    columns_post = ['J0802__101', 'J0802__102',  'J0802__103']
    adjustment_df1 = 100
    for col in columns_post:
        df1_post[col] *= adjustment_df1

    # Change the data type to a string
    df1_pre.year_wst = df1_pre.year_wst.astype(int)
    df1_post.year_wst_post = df1_post.year_wst_post.astype(int)

    # Merge two data frames
    df1 = df1_pre.merge(df1_post, how='outer',
                        left_on='year_wst', right_on='year_wst_post')

    # Create a column for the year
    df1['year_wst'] = df1.year_wst.fillna(0) + df1.year_wst_post.fillna(0)

    # Create a column dictionary
    columns_pair = {
        'J0802__001': 'J0802__101',
        'J0802__005': 'J0802__102',
        'J0802__006': 'J0802__103'}
    columns_pre = ['J0802__001', 'J0802__005', 'J0802__006']

    for col in columns_pre:
        df1[col] = df1[col].fillna(0) + df1[columns_pair[col]].fillna(0)

    df1 = df1[['year_wst', 'J0802__001', 'J0802__005', 'J0802__006']]

    # Select columns for df2
    # Agricultural product price index, 1934-36 = 100, 'J0810__004'
    # J0810__004 has two columns.
    # One is for 1874-1940 data, with 1934-36 = 100 and suffixed with '_1'.
    # The other is for 1950-1963 data, with 1934-36 = 1 and suffixed with '_2'.

    df2 = df2[['year_wst', 'J0810__004_1', 'J0810__004_2']]

    # Add two columns, adjusting to 1934-1936 = 100
    adjustment_df2 = 100
    df2['J0810__004'] = df2['J0810__004_1'].fillna(0) + \
        df2['J0810__004_2'].fillna(0) * adjustment_df2
    df2 = df2[['year_wst', 'J0810__004']]

    # Select columns for df3
    # Price Indexes of Manufacturfing and Mining Products, 'J0815__001'
    # J0815__001 has two columns.
    # One is for 1873-1945 data, with 1934-36 = 100 and suffixed with '_1'.
    # The other is for 1951-1962 data, with 1960 = 100 and suffixed with '_2'.
    # Pre-war data is not linked to post-war data.
    df3 = df3[['year_wst', 'J0815__001_1']]

    # Select columns for df4
    # Indexes of Investment Goods Prices
    # J0801__003 has two columns.
    # One is for 1874-1940 data, with 1934-36 = 100 and suffixed with '_1'.
    # The other is for 1950-1963 data, with 1960 = 1 and suffixed with '_2'.
    df4 = df4[['year_wst', 'J0801__003_1', 'J0801__003_2']]

    # Get the price index of 1955.
    value_1955 = df4_temp.iloc[97, -1]
    # When 1934-36 = 1, the 1955 link index is 359.7.
    linked_index_1955 = df4_temp.iloc[109, -1]
    # Multiply by 100 so that 1934-36 = 100.
    adjustment_df4 = linked_index_1955 / value_1955 * 100
    df4['J0801__003'] = df4['J0801__003_1'].fillna(0) + \
        df4['J0801__003_2'].fillna(0) * adjustment_df4
    df4 = df4[['year_wst', 'J0801__003']]

    # Set the column name
    df1.columns = ['year_wst', 'cpi_goods', 'cpi_agr', 'cpi_ind']
    df2.columns = ['year_wst', 'ppi_agr']
    df3.columns = ['year_wst', 'ppi_ind']
    df4.columns = ['year_wst', 'epi_inv']

    # Test
    # df1.to_csv('test1.csv')
    # df2.to_csv('test2.csv')
    # df3.to_csv('test3.csv')
    # df4.to_csv('test4.csv')

    # Merge data frames
    how = 'outer'
    on = 'year_wst'
    # df = pd.merge(pd.merge(pd.merge(df1, df2, how=how, on=on),
    #              df3, how=how, on=on), df4, how=how, on=on)
    df_merge1 = pd.merge(df1, df2, how=how, on=on)
    df_merge2 = pd.merge(df3, df4, how=how, on=on)
    df = pd.merge(df_merge1, df_merge2, how=how, on=on)
    df = df.sort_values(by=['year_wst'])

    # Save the dataframe to a csv file
    file_name = 'pre_CPI_link.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = '../../../Data/Downloaded/'
    main(output_folder)

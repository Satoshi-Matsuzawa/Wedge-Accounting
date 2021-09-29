#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd


def main(output_dest):
    # read csv files
    df_exp = pd.read_csv('../../Data/Downloads/Post/post_exp.csv')
    df_CPI = pd.read_csv('../../Data/Downloads/Post/post_CPI_alt.csv')

    # Convert CPIs so that 1990 price is 1
    cpi_goods_1990 = df_CPI.loc[df_CPI.year_wst == 1990]['cpi_goods'].values[0]
    cpi_agr_1990 = df_CPI.loc[df_CPI.year_wst == 1990]['cpi_agr'].values[0]
    df_CPI['cpi_goods_1990'] = df_CPI['cpi_goods'] / cpi_goods_1990
    df_CPI['cpi_agr_1990'] = df_CPI['cpi_agr'] / cpi_agr_1990

    # Merge dataframes
    df = df_exp[['year_wst', 'cons_pc', 'food_pc']].merge(
        df_CPI[['year_wst', 'cpi_goods_1990', 'cpi_agr_1990']], on='year_wst')

    # Create a column with real variables
    df['cons_pc_real'] = df['cons_pc'] / df['cpi_goods_1990']
    df['food_pc_real'] = df['food_pc'] / df['cpi_agr_1990']
    df['non_food_pc_real'] = df['cons_pc_real'] - df['food_pc_real']

    # Select columns with real variables
    df_real = df[['year_wst', 'cons_pc_real',
                  'food_pc_real', 'non_food_pc_real']].copy()
    df_real.columns = ['year_wst', 'cons', 'food', 'non_food']

    # Convert monthly data to annual data
    coeff = 12
    df_real['cons'] = df_real['cons'] * coeff
    df_real['non_food'] = df_real['non_food'] * coeff
    df_real['food'] = df_real['food'] * coeff

    # Save the dataframe to a csv file
    file_name = 'post_exp_pc_real.csv'
    output = output_dest + file_name

    df_real.to_csv(output, index=False)


if __name__ == '__main__':
    output_dest = ''
    main(output_dest)

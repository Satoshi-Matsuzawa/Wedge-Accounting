#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd


def main(output_dest):
    url = 'https://warp.da.ndl.go.jp/info:ndljp/pid/11423429/www.stat.go.jp/data/chouki/zuhyou/02-07.xls'
    df = pd.read_excel(url, header=None, index_col=None)

    # Select columns for Japanese calendar year, western calendar year,
    # total, urban and rural population.
    df = df.iloc[:, [0, 1, 2, 3, 4]]

    # Set the column name
    columns = ['year_jpn', 'year_wst', 'tot_pop', 'urban_pop', 'rural_pop']
    df.columns = columns

    # Trim the data frame
    df = df.iloc[9:1161, :]

    # Replace hyphen with zero
    df = df.replace('-', 0)

    # This dataset includes national and prefectural populations.
    # The data for each prefecture is saved vertically.
    # Create a dictionary where the key is the prefectural name and
    # the value is the starting and ending location of the prefectural data.
    num_of_pref = 48
    rows_btw_pref = 24
    rows_data = 23
    pref_row_init = 0

    pref_dict = {}

    for i in range(num_of_pref):
        pref_row = pref_row_init + i * rows_btw_pref
        pref_name = df.iloc[pref_row, 0].strip()

        data_start_loc = pref_row + 1
        data_end_loc = data_start_loc + rows_data
        pref_dict[pref_name] = data_start_loc, data_end_loc

    # Create a function to save the data of the selected prefecture
    def save_csv(pref_name, csv_pref_name, output_dest):
        pref_data_start = pref_dict[pref_name][0]
        pred_data_end = pref_dict[pref_name][1]
        # Get data for the selected prefecture
        # Delete the Japanese calendar year column
        df_temp = df.iloc[pref_data_start: pred_data_end, [1, 2, 3, 4]]
        csv_name = output_dest + 'urban_rural_pop_' + csv_pref_name + '.csv'
        df_temp.to_csv(csv_name, index=False)

    # Save the data for the selected prefecture
    save_csv('全国', 'total', output_dest)
    save_csv('東京都', 'tokyo', output_dest)
    save_csv('神奈川県', 'kanagawa', output_dest)
    save_csv('埼玉県', 'saitama', output_dest)
    save_csv('千葉県', 'chiba', output_dest)
    save_csv('愛知県', 'nagoya', output_dest)
    save_csv('京都府', 'kyoto', output_dest)
    save_csv('大阪府', 'osaka', output_dest)
    save_csv('兵庫県', 'hyogo', output_dest)


if __name__ == '__main__':
    output_dest = '../../../Data/Downloads/'
    main(output_dest)

#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd


def main(output_folder, results_folder):
    # read csv file
    file_mu = output_folder + 'pre_mu_ratio_static.csv'
    file_prd = output_folder + 'pre_labor_prd_ratio.csv'
    df_mu = pd.read_csv(file_mu)
    df_labor_prd = pd.read_csv(file_prd)
    df = df_mu.merge(df_labor_prd, on='year_wst').copy()

    df['labor_wedge'] = df['muM/PM/muA/PA'] * df['F_LM/F_LA']

    # Save the dataframe to a csv file
    file_name = 'pre_labor_w.csv'
    output = results_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = ''
    results_folder = ''
    main(output_folder, results_folder)

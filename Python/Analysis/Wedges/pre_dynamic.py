#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import params
import pandas as pd


def main(output_folder, results_folder):
    # read csv file
    file_mu = output_folder + 'pre_mu_ratio_dynamic.csv'
    file_prd = output_folder + 'pre_cap_prd_ratio.csv'
    df_mu = pd.read_csv(file_mu)
    df_cap_prd = pd.read_csv(file_prd)
    df = df_mu.merge(df_cap_prd, on='year_wst').copy()

    delta = params.delta
    beta = params.beta

    # Create a column for consumption growth
    df['cns_growth'] = 1 / df['cMt/cMt+1']

    # Compute real return on investment
    df['roi'] = 1 - delta + df['F_KM'].shift(-1)
    df['intertemporal_wedge'] = beta * df['cMt/cMt+1'] * df['roi']

    # Save the dataframe to a csv file
    file_name = 'pre_inter_w.csv'
    output = results_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    output_folder = ''
    results_folder = ''
    main(output_folder, results_folder)

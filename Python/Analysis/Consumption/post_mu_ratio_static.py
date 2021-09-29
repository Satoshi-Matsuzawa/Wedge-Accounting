#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import params
import pandas as pd
from . import cns_funcs as func


def main(input_folder, output_folder):
    # read csv file
    file = input_folder + 'post_exp_pc_real.csv'
    df = pd.read_csv(file)

    # For this analysis, we need to convert the gamma
    df_post_CPI = pd.read_csv('../../Data/Downloads/Post/post_CPI_alt.csv')
    df_CPI_link = pd.read_csv('../../Data/Downloads/Pre/pre_CPI_link.csv')

    # 100 yen in 1935 corresponds to the following value
    # Approximately 36071 yen at the 1955 price
    cpi_agr_link_1935_1955 = df_CPI_link.loc[df_CPI_link.year_wst ==
                                             1955]['cpi_agr'].values[0]

    # The CPI for agricultural products in 1955 and 1990 are as follows:
    cpi_agr_1955 = df_post_CPI.loc[df_post_CPI.year_wst ==
                                   1955]['cpi_agr'].values[0]
    cpi_agr_1990 = df_post_CPI.loc[df_post_CPI.year_wst ==
                                   1990]['cpi_agr'].values[0]
    cpi_agr_link_1955_1990 = cpi_agr_1990 / cpi_agr_1955

    # The following converts the gamma of the 1935 price to the 1990 price
    gammaA_1990 = params.gammaA / 100 * \
        cpi_agr_link_1935_1955 * cpi_agr_link_1955_1990

    PA_gammaA = gammaA_1990
    etaA = params.etaA
    etaM = params.etaM

    # Create a column for marginal utility ratio
    df = func.create_mu_ratio_static(df, PA_gammaA, etaA, etaM)

    # Save the dataframe to a csv file
    file_name = 'post_mu_ratio_static.csv'
    output = output_folder + file_name

    df.to_csv(output, index=False)


if __name__ == '__main__':
    input_folder = '../../Data/Downloads/Post/'
    output_folder = ''
    main(input_folder, output_folder)

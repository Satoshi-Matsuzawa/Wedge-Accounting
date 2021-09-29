#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import Consumption.pre_mu_ratio_dynamic as pre_mu_ratio_dynamic
import Consumption.pre_mu_ratio_static as pre_mu_ratio_static
import Consumption.post_mu_ratio_dynamic as post_mu_ratio_dynamic
import Consumption.post_mu_ratio_static as post_mu_ratio_static

import Production.post_labor_prd_ratio as post_labor_prd_ratio
import Production.pre_labor_prd_ratio as pre_labor_prd_ratio
import Production.pre_cap_prd_ratio as pre_cap_prd_ratio
import Production.post_cap_prd_ratio as post_cap_prd_ratio

# Address of the folder to save the data
output_folder_post = '../../Data/Analysis/Post/'
output_folder_pre = '../../Data/Analysis/Pre/'

# Address of the folder of saved files
input_folder_post = '../../Data/Downloads/Post/'
input_folder_pre = '../../Data/Downloads/Pre/'


def main():
    # Create mu ratios
    pre_mu_ratio_dynamic.main(input_folder_pre, output_folder_pre)
    pre_mu_ratio_static.main(input_folder_pre, output_folder_pre)
    post_mu_ratio_dynamic.main(input_folder_post, output_folder_post)
    post_mu_ratio_static.main(input_folder_post, output_folder_post)

    # Create productivity ratios
    post_labor_prd_ratio.main(input_folder_post, output_folder_post)
    post_cap_prd_ratio.main(input_folder_post, output_folder_post)
    pre_labor_prd_ratio.main(input_folder_pre, output_folder_pre)
    pre_cap_prd_ratio.main(input_folder_pre, output_folder_pre)


if __name__ == '__main__':
    main()

#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

# Import program for prewar data.
import Post.post_CPI as post_CPI
import Post.post_CPI_alt as post_CPI_alt
import Post.post_GDP as post_GDP
import Post.post_emp as post_emp
import Post.post_cap as post_cap
import Post.post_exp as post_exp
import Post.post_exp_real as post_exp_real
import Post.post_pop as post_pop

# Import program for postwar data.
import Pre.pre_GDP as pre_GDP
import Pre.pre_emp as pre_emp
import Pre.pre_exp as pre_exp
import Pre.pre_exp_pc as pre_exp_pc
import Pre.pre_pop as pre_pop
import Pre.pre_cap as pre_cap
import Pre.pre_CPI as pre_CPI
import Pre.pre_CPI_link as pre_CPI_link

# Address of the folder to save the data
output_folder_post = '../../Data/Downloads/Post/'
output_folder_pre = '../../Data/Downloads/Pre/'


def main():
    post_CPI.main(output_folder_post)
    post_CPI_alt.main(output_folder_post)
    post_GDP.main(output_folder_post)
    post_emp.main(output_folder_post)
    post_cap.main(output_folder_post)
    post_exp.main(output_folder_post)
    post_exp_real.main(output_folder_post)
    post_pop.main(output_folder_post)

    pre_GDP.main(output_folder_pre)
    pre_emp.main(output_folder_pre)
    pre_exp.main(output_folder_pre)
    pre_exp_pc.main(output_folder_pre)
    pre_pop.main(output_folder_pre)
    pre_cap.main(output_folder_pre)
    pre_CPI.main(output_folder_pre)
    pre_CPI_link.main(output_folder_pre)


if __name__ == '__main__':
    main()

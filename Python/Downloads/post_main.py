#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import Post.post_CPI as post_CPI
import Post.post_CPI_alt as post_CPI_alt
import Post.post_GDP as post_GDP
import Post.post_emp as post_emp
import Post.post_cap as post_cap
import Post.post_exp as post_exp
import Post.post_pop as post_pop
import Post.post_GDP_def as post_GDP_def


# Address of the folder to save the data
output_dest = '../../Data/Downloads/Post/'


def main():
    # post_CPI.main(output_dest)
    # post_CPI_alt.main(output_dest)
    # post_GDP.main(output_dest)
    post_emp.main(output_dest)
    # post_cap.main(output_dest)
    # post_exp.main(output_dest)
    # post_pop.main(output_dest)
    # post_GDP_def.main(output_dest)


if __name__ == '__main__':
    main()

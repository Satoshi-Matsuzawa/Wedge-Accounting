#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import Pre.pre_GDP as pre_GDP
import Pre.pre_emp as pre_emp
import Pre.pre_exp as pre_exp
import Pre.pre_exp_pc as pre_exp_pc
import Pre.pre_pop as pre_pop
import Pre.pre_cap as pre_cap
import Pre.pre_CPI as pre_CPI
import Pre.pre_CPI_link as pre_CPI_link


# Address of the folder to save the data
output_dest = '../../Data/Downloads/Pre/'


def main():
    # pre_GDP.main(output_dest)
    pre_emp.main(output_dest)
    # pre_exp.main(output_dest)
    # pre_exp_pc.main(output_dest)
    # pre_pop.main(output_dest)
    # pre_cap.main(output_dest)
    # pre_CPI.main(output_dest)
    # pre_CPI_link.main(output_dest)


if __name__ == '__main__':
    main()

#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import Facts.urban_rural_pop as facts_pop


# Address of the folder to save the data
output_dest = '../../../Data/Downloads/Facts/'


def main():
    facts_pop.main(output_dest)


if __name__ == '__main__':
    main()

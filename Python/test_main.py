#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd
import test


def main():
    url = "https://www.esri.cao.go.jp/jp/sna/data/data_list/minkan/files/tables/h7/0911stock.xls"
    df = pd.read_excel(url, header=None, index_col=None)
    df.to_csv('test.csv')
    test.sample_function()


if __name__ == '__main__':
    main()

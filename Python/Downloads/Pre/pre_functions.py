#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import pandas as pd


def create_cleaned_df(xl, sheet_name):
    df = xl.parse(sheet_name=sheet_name, header=None, index_col=None)
    df = drop_empty_columns_and_rows(df)
    rename_column_with_stat_id(df)
    df = get_rows_containing_data(df)
    return df


def drop_empty_columns_and_rows(df):
    return df.loc[df.notnull().sum(axis=1) > 2, df.notnull().sum() > 2]


def rename_column_with_stat_id(df):
    index = get_index_of_row_containing_stat_id(df)
    columns = df.loc[index].reset_index(drop=True).tolist()
    columns = rename_duplicates_in_list(columns)
    columns[0] = 'year_wst'
    df.columns = columns


def get_index_of_row_containing_stat_id(df):
    # All statistical IDs start with J.
    # Search from the second row
    index = df.index[df.iloc[:, 1].str.contains(r'^J', na=False)].tolist()[0]
    return index


def get_rows_with_digits(df):
    # Get rows with digts
    # Search from the first row
    rows_with_digits = df.iloc[:, 0].astype(str).str.isdigit().tolist()
    return rows_with_digits


def get_rows_containing_data(df):
    return df[get_rows_with_digits(df)]


def rename_duplicates_in_list(mylist):
    # Add underscores and progressive numbers to duplicate items in the list
    renamed_list = [str(v) + '_' + str(mylist[:i].count(v) + 1)
                    if mylist.count(v) >= 2 else v for i, v in enumerate(mylist)]
    return renamed_list

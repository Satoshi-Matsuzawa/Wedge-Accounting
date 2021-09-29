#!/usr/bin/env conda run -n jpandas python
# -*- coding: utf-8 -*-

import re


def drop_empty_columns_and_rows(df):
    return df.loc[df.notnull().sum(axis=1) > 2, df.notnull().sum() > 2]


def remove_whitespaces(df, column_name):
    df[column_name] = df[column_name].astype(
        str).map(lambda x: x.replace(' ', ''))
    df[column_name] = df[column_name].astype(
        str).map(lambda x: x.replace('\u3000', ''))


def replace_heisei_gannen(df, column_name):
    df[column_name] = df[column_name].astype(
        str).map(lambda x: x.replace('平成元年', '1'))


def remove_chinese_letters(df, column_name):
    df[column_name] = df[column_name].astype(
        str).map(lambda x: re.sub('[一-龥]', '', x))


def extract_numbers(df, column_name):
    df[column_name] = df[column_name].astype(
        str).map(lambda x: re.sub('[^0-9]', '', x))


def clean_year(df, column_name):
    remove_whitespaces(df, column_name)
    replace_heisei_gannen(df, column_name)
    extract_numbers(df, column_name)

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:49:51 2019
@author: ulrik
"""
import pandas as pd
import numpy as np
from django.conf import settings
# import time
#
#
# start_time = time.time()
url = 'https://www.vinmonopolet.no/medias/sys_master/products/products/hbc/hb0/8834253127710/produkter.csv'


def df_to_float_array(df, key):
    series = df[key].astype(float)
    return series.values


def df_to_series(df, key):
    return df[key]


def alkohol_per_kroner(alcohol, price, volume):
    return alcohol * volume / price


def get_max_index(array, number):
    ind = np.argpartition(array, -number)[-number:]
    ind = ind[np.argsort(array[ind])[::-1]]
    return ind


def sort(df, kind):
    return df[df.Varetype == kind]


def cheapest(kind, number):
    df = pd.read_csv('{}/products.csv'.format(settings.MEDIA_ROOT),
                     delimiter=';', encoding='unicode_escape',
                     index_col='Varenummer', usecols=[1, 2, 3, 4, 5, 6, 26, 27, 35], decimal=',',
                     dtype={'Alkohol': np.float64, 'Pris': np.float64, 'Volum': np.float64, }, memory_map=True)
    df = sort(df, kind)
    varenummer = df.index.values
    # pris = df_to_float_array(df, 'Pris')
    # alkohol = df_to_float_array(df, 'Alkohol')
    # volum = df_to_float_array(df, 'Volum')
    alkohol = df['Alkohol'].values
    pris = df['Pris'].values
    volum = df['Volum'].values
    score = alkohol_per_kroner(alkohol, pris, volum)
    score[np.isnan(score)] = 0
    index = get_max_index(score, number)
    chp_dict = {}
    a = 1
    for i in index:
        nummer = varenummer[i]
        chp_dict.update({str(a): [
            df['Varetype'][nummer], df['Varenavn'][nummer], df['Sukker'][nummer],
            df['Alkohol'][nummer], df['Literpris'][nummer], df['Vareurl'][nummer]
        ]}
        )  # Varetype, Varenavn, Sukker, Alkohol, Literpris, Vareurl
        a += 1
    return chp_dict


# d = cheapest('Rødvin', 10)
# for key, value in d.items():
#     print(key, value)
#
#
#
#
# print(time.time() - start_time)

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:52:51 2020

@author: Max
"""
import pandas as pd

def data_fill_from_df(data,fill_table,data_id): 
    """like vlookup, try to fill a table with another table as a reference"""
    for index, row in fill_table.iterrows():
        for col in fill_table.columns[1:]:
            data[col][data[data_id]==row[0]]=row[col]
    return data 


def fillna_with_preced_record(table,col,order_col):
    new_
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:58:58 2020

@author: Max
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def cor_heatmap(data):
    """give a heatmap of pearson coef between columns in the data table"""

    f, ax = plt.subplots(figsize=(10, 8))
    corr = data.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(240,10,as_cmap=True),
                square=True, ax=ax)
    
def distplot_compare(data,cat,num_col):
    """cat has to be binary"""
    f=plt.subplot(figsize=(12,5))
    
    ax=f.add_subplot(121)
    sns.distplot(data[(data[cat] == 1)][num_col],color='c',ax=ax)
    ax.set_title('Distribution of charges for %s',cat)
    
    ax=f.add_subplot(122)
    sns.distplot(data[(data[cat] == 0)][num_col],color='b',ax=ax)
    ax.set_title('Distribution of charges for non-%s',cat)
    
def cat_cat_bar(data,xcat,legendcat):
    sns.catplot(x=xcat,kind="count",hue=legendcat,palette="pink")
    
def cat_cat_num_bar(data,xcat,ynum,lengendcat):
    sns.catplot(x=xcat,y=ynum,kind="bar",hue=lengendcat,palette="Blues_d")   
    
def num_num_scater_joint_dist(data,num_1,num_2):
    f,ax = plt.subplots(figszie=(10,8))
    g = sns.jointplot(x=num_1, y=num_2, data = data,kind="kde", color="m")
    g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
    g.ax_joint.collections[0].set_alpha(0)
    g.set_axis_labels("$X$", "$Y$")
    ax.set_title('Distribution of %s and %s for the data'%(num_1,num_2))
    
    
    
    
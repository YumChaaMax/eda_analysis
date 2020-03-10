# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:45:24 2020

@author: Max
"""
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt
from datetime import datetime


def foreward_selection(X,y,model,score_back):
    """add one feature once,,to find best features
        input:
           X:featues to examine
           y:labels to predict
           model: model to use
           score_back: scoring, like precision_score,recall_score,accuracy_score
      return scores (ie.mean of accuracy scores of cv )
    """
    scores=dict()
    for feature in X.columns:
        temp_X=X[feature]
        temp_scores=cross_val_score(model, temp_X,y,cv=5,scoring=score_back)
        scores[feature]=np.mean(temp_scores)
        
    results=pd.DataFrame.from_dict(scores,orient='index')
    return results
    
def backward_elimination(X,y,model,score_back):
    """remove one feature once,to find best features
       input:
           X:featues to examine
           y:labels to predict
           model: model to use
           score_back: scoring, like precision_score,recall_score,accuracy_score
      return scores (ie.mean of accuracy scores of cv )
    """
    scores=dict()
    for feature in X.columns:
        temp_X=X.drop(columns=[feature])
        temp_scores=cross_val_score(model, temp_X,y,cv=5,scoring=score_back)
        scores[feature]=np.mean(temp_scores)
        
    results=pd.DataFrame.from_dict(scores,orient='index')
    
    return results

def cat_cat_plot(data,cat1,cat2,feature_title=None):
    """mosaic"""
    plot_data=data[[cat1,cat2]]
    mosaic(plot_data,[cat1,cat2],title=feature_title)
    plt.show()
    
def date_engineer(start_date,end_date):
    """compute month between two dates"""
    
    start_year=datetime.strptime(start_date,'%Y-%m-%d').year
    start_month=datetime.strptime(start_date,'%Y-%m-%d').month
    end_year=datetime.strptime(end_date,'%Y-%m-%d').year
    end_month=datetime.strptime(end_date,'%Y-%m-%d').month
    interval_month=(end_year-start_year)*12+(end_month-start_month)
    
    #interval_days=datetime.strptime(end_date,'%Y-%m-%d')-datetime.strptime(start_date,'%Y-%m-%d')
    return interval_month

def cat_num_boxplot(data,cat,num,is_sqrt=False):
    if is_sqrt:
        new_num=data[num].apply(np.sqrt)
        new_data=pd.concat([data[cat],new_num],axis=1)
        return new_data.boxplot(by=cat)
    else:
        return data[[cat,num]].boxplot(by=cat) 
    

        
    
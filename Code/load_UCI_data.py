# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:55:43 2021

@author: Abraham
"""

import os
from UCI_ML_API_master import UCI_ML_Functions as UCI

df_base = UCI.read_dataset_table()
df_base = UCI.clean_dataset_table(df_base,msg_flag=False)

df = UCI.build_full_dataframe()



df_base = df_base.merge(df, on="Name")


size = 'Small'
dataformat = 'csv'


def read_data(Size = 'Small',DataFormat='csv'):
    
    if type(Size) != list:
        Size = [Size]
    if type(DataFormat) != list:
        DataFormat = [DataFormat]
        
    for size in Size:
        for dataformat in DataFormat:
            url_list = df_base[df_base['Sample size']==size]['Datapage URL'].tolist()
            names_list = df_base[df_base['Sample size']==size]['Identifier string'].tolist()
            names_list = [name.replace('+','_').replace(' ','_') for name in names_list]
            
            right_len = len(dataformat)
            
            for name, url in zip(names_list,url_list):
                newpath = r'../Data/'+name 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                    
                UCI.download_dataset_url(url, newpath)
                
                dataformat_Search = True
                for datafile in os.listdir(newpath):
                    
                    if datafile[-right_len:]==dataformat and dataformat_Search:
                        preface_string = size+"_"+dataformat+"_"
                        os.rename(newpath,'../Data/'+preface_string+name)
                        dataformat_Search = False
                    else:
                        os.remove(newpath+'/'+datafile)
                        
                if dataformat_Search:
                    os.rmdir(newpath)

    

read_data(Size=['Small','Large'])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
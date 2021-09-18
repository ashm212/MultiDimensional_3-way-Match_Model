# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 17:32:59 2020
@author: ashu0
"""

import pandas as pd
from glob import glob

filenames = glob(r'C:\Users\ashu0\OneDrive\Desktop\Ok\Modeling\Three  Way Match\*.csv')
dataframes = [pd.read_csv(f) for f in filenames]

df_inv=dataframes[0]
df_po=dataframes[1]
df_receipt = dataframes[2]

df_connect_1=pd.merge(df_inv,df_po,how='left',left_on=['PO#'],right_on=['PO#'])
                                                       
df_connect_2=pd.merge(df_connect_1,df_receipt,how='left',left_on=['PO#'],right_on=['Authorizing PO #'])  
                                                                  
dfinvoice_sum=df_connect_2.groupby("PO#")["Inv Amt","Inv Qty"].sum()

df_connect_3= pd.merge(df_connect_2,dfinvoice_sum,how='left',left_on=['PO#'],right_on=['PO#'])    

#The quantity billed must be less than or equal to the quantity ordered
#The invoice price must be less than or equal to the purchase order price
#The quantity billed must be less than or equal to the quantity received                                                                     

                                                                      
df_connect_3['Is_Qty_Billed<=Qty_Recieved?']=df_connect_3['Inv Qty_y']<=df_connect_3['PO Qty']

df_connect_3['Is_Amt_Billed<=PO Amt?']=df_connect_3['Inv Amt_y']<=df_connect_3['PO Amt']

df_connect_3['Is_Amt_Billed<=Amt_Recieved?']=df_connect_3['Inv Qty_y']<=df_connect_3['Qty of Each Item Rec']

df_connect_3.to_csv(r'C:\Users\ashu0\OneDrive\Desktop\Ok\3-way-match.csv')

                                                       


                                                     
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data={
    'name':['alice','bob','charlie',None,'eve'],
    'age':[25,None,30,22,None],
    'city':['new york','los angeles',None,'chicago','miami'],
    
}
df=pd.DataFrame(data)
def analyze_missing_data(df):
    print("DataFrame:")
    print(df)
    print("\nmissing data analysis:")
    missing_data=df.isnull().sum()
    print("missing values in each column:")
    print(missing_data[missing_data>0])
    missing_percentage=(missing_data/len(df))*100
    print("\npercentage of missing values in each column:")
    print(missing_percentage[missing_percentage>0])
    return missing_data,missing_percentage

def handle_missing_data(df):
    print("\n choose a method to handle missing data:")
    print("1.fill missing values with a specific value:")
    print("2.drop rows with missing values")
    print("3.drop columns with missing values")
    choice=input("enter your choice(1/2/3):")
    if choice=='1':
        value=input("enter the valueto fill missing data:")
        df_filled=df.fillna(value)
        print("\ndata after filling missing values:")
        print(df_filled)
    elif choice=='2':
        df_dropped_rows=df.dropna()
        print("\ndata after dropping rows with missing values:")
        print(df_dropped_rows)
    elif choice=='3':
        df_dropped_columns=df.dropna(axis=1)
        print("\ndata after dropping columns with missing values:")
        print(df_dropped_columns)
    else:
        print("invalid choice! please enter 1,2or3")
missing_data,missing_percentage=analyze_missing_data(df)
handle_missing_data(df)


# In[ ]:





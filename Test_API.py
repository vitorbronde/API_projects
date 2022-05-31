#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests


# ### Question 1

# In[2]:


number_per_pages = int(input("select the number of pages: "))

url= 'https://reqres.in/api/users?'

parameters={
    'per_page': number_per_pages,
}

api = requests.get(url , params=parameters)
dictionary = api.json()

parameters2={
    'page'  : dictionary['total_pages'] ,
    'per_page': number_per_pages,
}

api = requests.get(url , params=parameters2)
dictionary2 = api.json()


base1 , base2 = pd.json_normalize(dictionary['data']) , pd.json_normalize(dictionary2['data'])
base1 , base2 = pd.DataFrame(data =base1) , pd.DataFrame(data =base2)

final_base  = pd.concat([base1 , base2]).reset_index()
file_name = input("Define the file´s name: ")
final_base.to_csv(file_name, index=False)


# ### Question 2

# In[3]:


user_id = int(input("Chose the user ID : ", ))


# In[4]:


if user_id in range(11):
    url= 'https://reqres.in/api/users?'
    parameters={
       'id': user_id,
        }
    api = requests.get(url , params=parameters)
    dictionary = api.json()
    df_nested_list = pd.json_normalize(dictionary['data'])
    df_nested_list = pd.DataFrame(data =df_nested_list)
    first_name ,last_name   = str(df_nested_list['first_name'].values) , str(df_nested_list['last_name'].values)
    first_name , last_name  = first_name.replace("'","") , last_name.replace("'","")
    first_name , last_name  = first_name.strip('[]') , last_name.strip('[]')
    Name = first_name+' '+last_name 
    print(Name)
else:
    print("Unidentified user, please try again ")


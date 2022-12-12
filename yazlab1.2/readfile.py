import tkinter
import pandas as pd
from tkinter import *
import nltk 
from nltk.corpus import stopwords
stop = stopwords.words('english')

my_filtered_csv = pd.read_csv('file.csv', usecols=['Product', 'Issue','Company','State','ZIP code','Complaint ID'])
my_filtered_csv['Product'] = my_filtered_csv['Product'].str.replace(r'[^\w\s]+', '',regex=True)
my_filtered_csv['Issue'] = my_filtered_csv['Issue'].str.replace(r'[^\w\s]+', '',regex=True)
my_filtered_csv['Company'] = my_filtered_csv['Company'].str.replace(r'[^\w\s]+', '',regex=True)
my_filtered_csv['State'] = my_filtered_csv['State'].str.replace(r'[^\w\s]+', '',regex=True)
my_filtered_csv['Company'] = my_filtered_csv['Company'].str.replace(' OF ', '')

my_filtered_csv.dropna()  

my_filtered_csv['Product'] = my_filtered_csv['Product'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))  #stop word kaldırma
my_filtered_csv['Issue'] = my_filtered_csv['Issue'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))  #stop word kaldırma
my_filtered_csv['Company'] = my_filtered_csv['Company'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))  #stop word kaldırma


my_filtered_csv.to_csv('currentfile.csv') #yeni csv ye atma




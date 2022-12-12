import pandas as pd
from fuzzywuzzy import process, fuzz
from scipy.spatial.distance import pdist, squareform
from difflib import SequenceMatcher
import threading
import time


df = pd.read_csv('rowsnew.csv', usecols=['Product', 'Issue','Company','State','ZIP code','Complaint ID'])
df2 = pd.read_csv('rowsnew.csv', usecols=['Product', 'Issue','Company','State','ZIP code','Complaint ID'])

complaintid="3198084"

row1=5

for i in range(2000):
    a=df.at[int(i),"Complaint ID"]
    for j in range(2000):
        b=df.at[int(j),"Complaint ID"]
        if(str(a)==str(b) and a!=b):
            print(str(i)+" "+str(j))
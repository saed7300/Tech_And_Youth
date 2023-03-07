# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 09:27:37 2023

@author: sneaz
"""
import pandas as pd
import os
import numpy as np
import csv
import nltk
from nltk.corpus import stopwords
print(stopwords.words('english'))

path_parenting = r"C:\Users\sneaz\Documents\Text Mining\Data\Corpus\Parenting"
path_society= r"C:\Users\sneaz\Documents\Text Mining\Data\Corpus\In Society"
path_health = r"C:\Users\sneaz\Documents\Text Mining\Data\Corpus\Mental Health"
path_education = r"C:\Users\sneaz\Documents\Text Mining\Data\Corpus\Education"

transaction_csv_label = r"C:\Users\sneaz\Documents\Text Mining\Data\Transaction Data\transaction_data_label.csv"
transaction_csv = r"C:\Users\sneaz\Documents\Text Mining\Data\Transaction Data\transaction_data.csv"
transaction_csv_parenting = r"C:\Users\sneaz\Documents\Text Mining\Data\Transaction Data\transaction_data_parenting.csv"
transaction_csv_education = r"C:\Users\sneaz\Documents\Text Mining\Data\Transaction Data\transaction_data_education.csv"
transaction_csv_insoc = r"C:\Users\sneaz\Documents\Text Mining\Data\Transaction Data\transaction_data_insociety.csv"
transaction_csv_mh = r"C:\Users\sneaz\Documents\Text Mining\Data\Transaction Data\transaction_data_mentalhealth.csv"

with open (transaction_csv_label,'w') as f:
    pass
with open (transaction_csv,'w') as f:
    pass
with open (transaction_csv_parenting,'w') as f:
    pass
with open (transaction_csv_education,'w') as f:
    pass
with open (transaction_csv_insoc,'w') as f:
    pass
with open (transaction_csv_mh,'w') as f:
    pass

corp_dict = {path_parenting: 'parenting', path_health: 'mental health', path_society:'in society', path_education: 'education'}
for key in corp_dict:
    #print(key)
    print(corp_dict[key])
    path=key
    label=corp_dict[key]
    file_names = []
    for name in os.listdir(path):
        #print(path+ "\\" + name)
        next1=path+ "\\" + name
        #file_names.append(next1)
        with open(next1, "r") as f:
            lines = f.read().split()
            #print(lines)
        with open(transaction_csv, 'a') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(lines)
        if label == 'education':
            with open(transaction_csv_education, 'a') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(lines)
        if label == 'parenting':
            with open(transaction_csv_parenting, 'a') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(lines)
        if label == 'in society':
            with open(transaction_csv_insoc, 'a') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(lines)
        if label == 'mental health':
            with open(transaction_csv_mh, 'a') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(lines)
        with open(transaction_csv_label, 'a') as f:
            csv_writer = csv.writer(f)
            lines.append(label)
            csv_writer.writerow(lines)
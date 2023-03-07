# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:30:44 2023

@author: sneaz
"""

import requests 

import pandas as pd
import os
import time

from newscatcherapi import NewsCatcherApiClient

newscatcherapi = NewsCatcherApiClient(x_api_key='wONxUo1NtAD1seyDbQkvHTbmeaiJmxZ7jJ_fjCqS9ok')

query_list = ['(tech OR technology) AND (children OR kids)',
              '(tech OR technology) AND (children OR kids) AND (school OR education)',
              '(phones OR tablets) AND (children OR kids)',
              '(computers OR video games) AND (children Or kids)'
               '(social media OR instagram) AND (children OR kids)',
               '(snapchat OR tik tok) AND ((children OR kids))'] 
   
full_dic2 = {
    'Title': [],
    'Topic': [],
    'Excerpt': [],
    'Summary': []
    }            
full_df2 = pd. DataFrame. from_dict(full_dic2)

for q_item in query_list:
    print(q_item)
    time.sleep(1)
    all_articles = newscatcherapi.get_search(q= q_item,
                                             lang='en',
                                             page_size=100)
    for articles in all_articles['articles']:
        print(articles['title'])
        update = {
            'Title': articles['title'],
            'Topic': articles['topic'],
            'Excerpt': articles['excerpt'],
            'Summary': articles['summary'],
            } 
        full_df2 = full_df2.append(update, ignore_index=True)
        
clean_df2 = full_df2.drop_duplicates()

clean_df2.to_csv(r'C:\Users\sneaz\Documents\Text Mining\Data\Data from API\NewsCatcher_text.csv',
                   index=False)
all_articles = newscatcherapi.get_search(q= 'dogs',
                                         lang='en',
                                         page_size=3)
for articles in all_articles['articles']:
    print(articles)
    print (articles['title'])
    print(articles['excerpt'])



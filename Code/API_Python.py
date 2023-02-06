# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 19:40:07 2023

@author: sneaz
"""

import requests 

import pandas as pd
import os

import time


#News API
secret_newsapi = '0519334c95a045b0a51e3747d7bcfc3d'

url_newsapi = 'https://newsapi.org/v2/everything?'


empty_dict_newsapi = {
    'Tech Source': [],
    'Tech Relation' : [],
    'API Source': [],
    'Source Name': [],
    'Title': [],
    'Author': [],
    'Source Description': [],
    'Source Content': [],
    'Publish Date': []
    }

newsapi_df = pd. DataFrame. from_dict(empty_dict_newsapi)


not_in = 'NOT (M3GAN OR Blumhouse)'
activity_list = ['children',
                 'teens',
                 'mental health',
                 'parenting',
                 '(K-12 OR schools)']

               
tech_list = ['technology', 'video Games', 'social media',
             '(tablet OR iPad OR iPhone OR smart phone)', 'e learning']



parameters = {
    'q': 'Technology AND Children AND Good', # query phrase
    'apiKey': secret_newsapi, # your own API key
    'searchIn': 'title,description',
    'sortBy': 'relevancy',
    'language': 'en'
    }
response = requests.get(url_newsapi, params=parameters)
response_json = response.json()

for t in tech_list:
    for i in activity_list:
        api_source = 'NewsAPI'
        activity_query = i
        tech_query = t
        query_string = tech_query + ' AND ' + activity_query + ' ' + not_in
        print(query_string)
        
        parameters = {
            'q': query_string, # query phrase
            'apiKey': secret_newsapi, # your own API key
            'searchIn': 'title,description',
            'sortBy': 'relevancy',
            'language': 'en'
            }
        response = requests.get(url_newsapi, params=parameters)
        response_json = response.json()
        for j in response_json['articles']:
            source_name = j['source']['name']
            title = j['title']
            author = j['author']
            description = j['description']
            content = j['content']
            publish_date = j['publishedAt']
            
            updating_dict = {
                'Tech Source': tech_query,
                'Tech Relation' : activity_query,
                'API Source': api_source,
                'Source Name': source_name,
                'Title': title,
                'Author': author,
                'Source Description': description,
                'Source Content': content,
                'Publish Date': publish_date
                }
            newsapi_df = newsapi_df.append(updating_dict, ignore_index=True)
        
    
newsapi_df.to_csv(r'C:\Users\sneaz/Documents\Text Mining\Data from API\NewsAPI_text.csv',
                  index=False)

#Bing News API
url_bingnews = "https://bing-news-search1.p.rapidapi.com/news/search"
headers = {
	"X-BingApis-SDK": "true",
	"X-RapidAPI-Key": "7d308cefcdmshf5104a6819d8c27p1d1442jsnb0663aaa71d7",
	"X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
}

empty_dict_newsapi = {
    'Tech Source': [],
    'Tech Relation' : [],
    'API Source': [],
    'Source Type': [],
    'Source Name':[],
    'Title': [],
    'Source Description': [],
    'Publish Date': []
    }

bingnews_df = pd. DataFrame. from_dict(empty_dict_newsapi)

for t in tech_list:
    for i in activity_list:
        api_source = 'Bing News API'
        activity_query = i
        tech_query = t
        query_string = tech_query + ' AND ' + activity_query + ' ' + not_in
        print(query_string)
        querystring = {"q":query_string,
                       "textFormat":"Raw",
                       "safeSearch":"Off"}
        time.sleep(10)
        response = requests.request("GET",
                                    url_bingnews,
                                    headers=headers,
                                    params=querystring)
        response_json = response.json()
        print(response_json)
        for j in response_json['value']:
            #print(j)
            article_name = j['name']
            news_type = j['_type']
            source_name = j['provider'][0]['name']
            article_discription = j['description']
            date_published = j['datePublished']
            updating_dict = {
                'Tech Source': tech_query,
                'Tech Relation' : activity_query,
                'API Source': api_source,
                'Source Type': news_type,                
                'Source Name': source_name,
                'Title': article_name,
                'Source Description': article_discription,
                'Publish Date': date_published
                }
            bingnews_df = bingnews_df.append(updating_dict, ignore_index=True)

bingnews_df.to_csv(r'C:/Users/sneaz/Documents\Text Mining\Data from API\BingNewsAPI_text.csv',
                   index=False)

print(response_json)

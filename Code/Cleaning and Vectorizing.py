# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:43:53 2023

@author: sneaz
"""

import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer 
import os, shutil
import nltk
nltk.download('wordnet')
nltk.download('words')
words = set(nltk.corpus.words.words())
stemmer=PorterStemmer()
lemmatizer = WordNetLemmatizer()

#Labels = ['Parenting', 'Mental Health', 'Education', 'In Society']
vector_path = r'C:\Users\sneaz\Documents\Text Mining\Vectors'

path_parenting = r"C:\Users\sneaz\Documents\Text Mining\Parenting"
path_society= r"C:\Users\sneaz\Documents\Text Mining\In Society"
path_health = r"C:\Users\sneaz\Documents\Text Mining\Mental Health"
path_education = r"C:\Users\sneaz\Documents\Text Mining\Education"


# for filename in os.listdir(path_education):
#     file_path = os.path.join(path_education, filename)
#     try:
#         if os.path.isfile(file_path) or os.path.islink(file_path):
#             os.unlink(file_path)
#         elif os.path.isdir(file_path):
#             shutil.rmtree(file_path)
#     except Exception as e:
#         print('Failed to delete %s. Reason: %s' % (file_path, e))

#stemming
def stemmer_clean(text_data):       
    words = text_data.split(' ')   
    text_data = [stemmer.stem(word) for word in words]
    text_data = ' '.join(text_data)
    return text_data

def lemmer_clean(text_data):
    words = text_data.split(' ') 
    #words = re.sub(r"[a-zA-Z]+", " ", text_data).lower().split(' ')    
    text_data = [lemmatizer.lemmatize(word) for word in words]
    text_data = ' '.join(text_data)
    return text_data


#Corpus def
def corpus_path(data, source_name, description_name):
    x=1
    y=1
    z=1
    w=1
    for index, row in data.iterrows():
        label = row['Label']
        description = row[description_name]
        if label == 'Parenting':
            txt_num = source_name+label+str(x)+".txt"
            file_path = os.path.join(path_parenting, txt_num)
            with open(file_path, "w", encoding="utf-8") as outfile:
                outfile.write(description)
            x=x+1
        if label == 'Education':
            txt_num = source_name+label+str(x)+".txt"
            file_path = os.path.join(path_education, txt_num)
            with open(file_path, "w", encoding="utf-8") as outfile:
                outfile.write(description)
            y=y+1
        if label == 'In Society':
            txt_num = source_name+label+str(x)+".txt"
            file_path = os.path.join(path_society, txt_num)
            with open(file_path, "w", encoding="utf-8") as outfile:
                outfile.write(description)
            z=z+1
        if label == 'Mental Health':
            txt_num = source_name+label+str(x)+".txt"
            file_path = os.path.join(path_health, txt_num)
            with open(file_path, "w", encoding="utf-8") as outfile:
                outfile.write(description)
            w=w+1

news_apis = pd.read_csv(r'C:\Users\sneaz\Documents\Text Mining\Data from API\NewsAPI_text_labled.csv')
news_clean =news_apis
for index, row in news_clean.iterrows():
    #print(row['Source Description'])
    clean_text = row['Source Description']
    print(clean_text)
    print(type(clean_text))
    print(type(clean_text))    
    clean_text = re.sub("[^a-zA-Z]+", " ", clean_text,0,re.IGNORECASE) 
    clean_text = stemmer_clean(clean_text)
    clean_text = lemmer_clean(clean_text)
    print(clean_text)
    clean_text =  " ".join(w for w in nltk.wordpunct_tokenize(clean_text)\
                           if w.lower() in words or not w.isalpha())
    clean_text = clean_text.lower()
    news_clean.at[index,'Source Description'] = clean_text
    
corpus_path(data=news_clean, source_name='newsapi', description_name='Source Description')

    
bingnews_apis = pd.read_csv(r'C:\Users\sneaz\Documents\Text Mining\Data from API\BingNewsAPI_text_labled.csv')
bing_clean = bingnews_apis
for index, row in bing_clean.iterrows():
    #print(row['Source Description'])
    clean_text = row['Source Description']
    clean_text = re.sub("[^a-zA-Z]+", " ", clean_text,0,re.IGNORECASE) 
    clean_text = stemmer_clean(clean_text)
    clean_text = lemmer_clean(clean_text)
    print(clean_text)
    clean_text =  " ".join(w for w in nltk.wordpunct_tokenize(clean_text)\
                           if w.lower() in words or not w.isalpha())
    clean_text = clean_text.lower()
    bing_clean.at[index,'Source Description'] = clean_text
    
corpus_path(data=bing_clean, source_name='bingapi', description_name='Source Description')

    
###Reddit
#subreddit_list ={'Technology': ['parenting', 'children', 'children mental health', 'children social media'],
 #                'Parenting': ['technology', 'children social media' ,'tablets', 'child iphone', 'video games', 'school technology']}

reddit_text = pd.read_csv(r'C:\Users\sneaz\Documents\Text Mining\Data from API\Reddit.csv')
reddit_text['Label']=""
#Create the lables
for index, row in reddit_text.iterrows():    
    if row['Subreddit Search'] == 'children mental health':
        label = 'Mental Health'
    elif row['Subreddit Search'] == 'children social media':
       label =  'In Society'
    elif row['Subreddit Search'] == 'children':
       label =  'In Society'
    elif row['Subreddit Search'] == 'parenting':
        label = 'Parenting'
    elif row['Subreddit Search'] == 'technology':
        label = 'Parenting'
    elif row['Subreddit Search'] == 'school technology':
        label = 'Education'
    else:
        label = 'Parenting'
    reddit_text.at[index,'Label'] = label


reddit_clean = reddit_text
reddit_clean['Subreddit Text'] = reddit_clean['Subreddit Text'].astype(str)
reddit_clean['Title'] = reddit_clean['Title'].astype(str)
#Cleaning Title Names
for index, row in reddit_clean.iterrows():
    print(row['Title'])
    for k in row['Title'].split("\n"):
        clean_text = re.sub(r"[^a-zA-Z]+", ' ', k)
    print(clean_text)
    reddit_clean.at[index,'Title'] = clean_text

#Cleaning Text
print(reddit_clean.info())

for index, row in reddit_clean.iterrows():
    if row['Subreddit Text'] == "":
        continue
    else:
        print(row['Subreddit Text'])
        for k in row['Subreddit Text'].split("\n"):
            clean_text = re.sub(r"[^a-zA-Z]+", ' ', k)
        print(clean_text)
        clean_text = re.sub("[^a-zA-Z]+", " ", clean_text,0,re.IGNORECASE) 
        clean_text = stemmer_clean(clean_text)
        clean_text = lemmer_clean(clean_text)
        print(clean_text)
        clean_text =  " ".join(w for w in nltk.wordpunct_tokenize(clean_text)\
                               if w.lower() in words or not w.isalpha())
        clean_text = clean_text.lower()
        reddit_clean.at[index,'Subreddit Text'] = clean_text
        
c = (reddit_clean['Subreddit Text'] == 'nan').sum()
print(c)

reddit_subtexts = reddit_clean[reddit_clean['Subreddit Text'] != ""]
reddit_subtexts = reddit_subtexts.dropna(how='all')
reddit_subtexts = reddit_subtexts[reddit_subtexts['Subreddit Text'] != "nan"]



corpus_path(data=reddit_subtexts, source_name='reddit', description_name='Subreddit Text')

#Vectorizing
#Parenting
corp_dict = {path_parenting: 'parenting', path_health: 'mental health', path_society:'in society', path_education: 'education'}
for key in corp_dict:
    print(key)
    print(corp_dict[key])
    path=key
    label=corp_dict[key]
    file_names = []
    for name in os.listdir(path):
        #print(path+ "\\" + name)
        next1=path+ "\\" + name
        file_names.append(next1)
    
    ###TfidfVectorizor
    my_vector_tf = TfidfVectorizer(input='filename', stop_words="english", max_df=.80, min_df=.01, max_features=100)
    vector_tran = my_vector_tf.fit_transform(file_names)
    col_names = my_vector_tf.get_feature_names()
    df_tf = pd.DataFrame(vector_tran.toarray(), columns = col_names)
    df_tf['Label']=label
    print(df_tf)
    file_name = label+"tf"+".csv"
    file_path = os.path.join(vector_path, file_name)
    df_tf.to_csv(file_path, index=False)
    
    my_vector_cv = CountVectorizer(input='filename', stop_words="english", max_df=.80, min_df=.01, max_features=100)
    vector_tran = my_vector_cv.fit_transform(file_names)
    col_names = my_vector_cv.get_feature_names()
    df_cv = pd.DataFrame(vector_tran.toarray(), columns = col_names)
    df_cv['Label']=label
    print(df_cv)
    file_name = label+"cv"+".csv"
    file_path = os.path.join(vector_path, file_name)
    df_cv.to_csv(file_path, index=False)


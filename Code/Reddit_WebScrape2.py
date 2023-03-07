# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:23:07 2023

@author: sneaz
"""
import praw
import pandas as pd

redit_clientid = 'ack1Zw44wlKRJIhgAi6l_Q'
redit_apikey = 'EcpWt8p_jTkdRhnoiCJhTXHzTd85jw'

##Web Scrape

reddit = praw.Reddit(client_id=redit_clientid, client_secret=redit_apikey, user_agent='EducationAPI')

subreddit_list ={'Technology': ['parenting', 'children', 'children mental health', 'children social media'],
                 'Parenting': ['technology', 'children social media' ,'tablets', 'child iphone', 'video games', 'school technology']}
empty_dict = {
    'Subreddit Name':[],
    'Subreddit Search': [],
    'ID':[],
    'Title':[],
    'Subreddit Text':[]
    }

reddit_df = pd.DataFrame(empty_dict)

subreddit_post = reddit.subreddit("Parenting")
resp = subreddit_post.search("tech toys")
for submission in resp:
    for top_level_comment in submission.comments:
        print(submission.title)
        print(top_level_comment.body)
print(resp.comments)

for sub_name in subreddit_list:
    print(sub_name)
    for search_name in subreddit_list[sub_name]:
        print(search_name)
        subreddit_post = reddit.subreddit(sub_name)
        resp = subreddit_post.search(search_name)
        for submission in resp:
            ID = submission.id
            TitleName = submission.title
            Text = submission.selftext
            update_dict = {
                'Subreddit Name':sub_name,
                'Subreddit Search': search_name,
                'ID':ID,
                'Title':TitleName,
                'Subreddit Text':Text
                }

            reddit_df = reddit_df.append(update_dict, ignore_index=True)

  
reddit_df.to_csv(r'C:\Users\sneaz\Documents\Text Mining\Data from API\Reddit.csv',
                  index=False)


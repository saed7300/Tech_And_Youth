# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:58:07 2023

@author: sneaz
"""
from sklearn.decomposition import LatentDirichletAllocation 
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import pyLDAvis.sklearn as LDAvis
import pyLDAvis
import pyLDAvis.gensim as gensimvis
from gensim import corpora, models, similarities 
import gensim
import re



path_parenting = r"C:\Users\sneaz\Documents\Text Mining\Data\Corpus\Parenting"
path_society= r"C:\Users\sneaz\Documents\Text Mining\Data\Corpus\In Society"
path_health = r"C:\Users\sneaz\Documents\Text Mining\Data\Corpus\Mental Health"
path_education = r"C:\Users\sneaz\Documents\Text Mining\Data\Corpus\Education"

corp_dict = {path_parenting: 'parenting', path_health: 'mental health', path_society:'in society', path_education: 'education'}
file_names = []
text_data = []
for key in corp_dict:
    print(key)
    print(corp_dict[key])
    path=key
    label=corp_dict[key]
    for name in os.listdir(path):
        #print(path+ "\\" + name)
        next1=path+ "\\" + name
        file_names.append(next1)
        with open(next1, "r") as f:
            lines = f.read()
            text_data.append(lines)
        
my_vector_cv = CountVectorizer(input='filename', stop_words="english", max_df=.80, min_df=.01, max_features=100)
vector_tran = my_vector_cv.fit_transform(file_names)
col_names = my_vector_cv.get_feature_names_out()
df_cv = pd.DataFrame(vector_tran.toarray(), columns = col_names)
print(col_names)

NUM_TOPICS=4
lda_model = LatentDirichletAllocation(n_components=NUM_TOPICS, max_iter=10, learning_method='online')
#lda_model = LatentDirichletAllocation(n_components=NUM_TOPICS, max_iter=10, learning_method='online')
top_n=10
lda_Z_DF = lda_model.fit_transform(df_cv)
print(lda_Z_DF.shape)  # (NO_DOCUMENTS, NO_TOPICS)
# for idx, topic in enumerate(lda_model.components_):
#     print(idx)
#     print(topic)
#     print([(my_vector_cv.get_feature_names()[i], topic[i])
#                 for i in topic.argsort()[:-top_n - 1:-1]])


def print_topics(model, vectorizer, top_n=10):
    for idx, topic in enumerate(model.components_):
        print("Topic %d:" % (idx))
        print([(vectorizer.get_feature_names_out()[i], topic[i])
                    for i in topic.argsort()[:-top_n - 1:-1]])
 
print("LDA Model:")
print_topics(lda_model, my_vector_cv)

res = [re.split(' ', s) for s in text_data]
dictionary = corpora.Dictionary(res)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in res]

lda = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word = dictionary, passes=20)

vis_data = gensimvis.prepare(lda, corpus, dictionary)
#pyLDAvis.show(vis_data)
pyLDAvis.save_pdf(vis_data, "lda_viz.pdf")

word_topic = np.array(lda_model.components_)
#print(word_topic)
word_topic = word_topic.transpose()

num_top_words = 10
vocab_array = np.asarray(col_names)

#fontsize_base = 70 / np.max(word_topic) # font size for word with largest share in corpus
fontsize_base = 12

for t in range(NUM_TOPICS):
    plt.subplot(1, NUM_TOPICS, t + 1)  # plot numbering starts with 1
    plt.ylim(0, num_top_words + 0.5)  # stretch the y-axis to accommodate the words
    plt.xticks([])  # remove x-axis markings ('ticks')
    plt.yticks([]) # remove y-axis markings ('ticks')
    plt.title('Topic #{}'.format(t))
    top_words_idx = np.argsort(word_topic[:,t])[::-1]  # descending order
    top_words_idx = top_words_idx[:num_top_words]
    top_words = vocab_array[top_words_idx]
    top_words_shares = word_topic[top_words_idx, t]
    for i, (word, share) in enumerate(zip(top_words, top_words_shares)):
        plt.text(0.3, num_top_words-i-0.5, word, fontsize=fontsize_base)
                 ##fontsize_base*share)

plt.tight_layout()
plt.show()
plt.savefig("TopicsVis.pdf")

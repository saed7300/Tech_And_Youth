# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 20:24:01 2023

@author: sneaz
"""
import pandas as pd
import os
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
from kmodes.kmodes import KModes
from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.metrics.pairwise import cosine_similarity

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



MyDict={}
for i in range(0, len(file_names)):
    MyDict[i] = file_names[i]

print("MY DICT:", MyDict)
        
df_cv=df_cv.rename(MyDict, axis="index")

kmeans_object_Count = KMeans(n_clusters=4)
#print(kmeans_object)
k_fit = kmeans_object_Count.fit(df_cv)


labels = kmeans_object_Count.labels_
prediction_kmeans = kmeans_object_Count.predict(df_cv)
#print(labels)
print(prediction_kmeans)

print("Silhouette Score for k = 4\n",silhouette_score(df_cv, prediction_kmeans))

# Format results as a DataFrame
Myresults = pd.DataFrame([df_cv.index,labels]).T
print(Myresults)


print(df_cv)
print(df_cv["child"]) 
x=df_cv["bad"]  ## col 6  
y=df_cv["help"]    ## col 29
z=df_cv["technology"]  ## col 74
colnames=df_cv.columns
print(colnames)

fig1 = plt.figure(figsize=(12, 12))
ax1 = Axes3D(fig1, rect=[0, 0, .90, 1], elev=48, azim=134)

ax1.scatter(x,y,z, cmap="RdYlGn", edgecolor='k', s=200,c=prediction_kmeans)
ax1.w_xaxis.set_ticklabels([])
ax1.w_yaxis.set_ticklabels([])
ax1.w_zaxis.set_ticklabels([])

ax1.set_xlabel('bad', fontsize=25)
ax1.set_ylabel('help', fontsize=25)
ax1.set_zlabel('technology', fontsize=25)
#plt.show()

df_cv.columns.get_loc("technology")

centers = kmeans_object_Count.cluster_centers_
print(centers)
#print(centers)
C1=centers[0,(6,29,74)]
print(C1)
C2=centers[1,(6,29,74)]
C3=centers[2,(6,29,74)]
C4=centers[3,(6,29,74)]
print(C2)
xs=C1[0],C2[0],C3[0],C4[0]
print(xs)
ys=C1[1],C2[1],C3[1],C4[1]
zs=C1[2],C2[2],C3[2],C4[2]


ax1.scatter(xs,ys,zs, c='black', s=2000, alpha=0.2)
plt.show()






kmeans_object_Count = KMeans(n_clusters=3)
#print(kmeans_object)
k_fit = kmeans_object_Count.fit(df_cv)


labels = kmeans_object_Count.labels_
prediction_kmeans = kmeans_object_Count.predict(df_cv)
#print(labels)
print(prediction_kmeans)

print("Silhouette Score for k = 3\n",silhouette_score(df_cv, prediction_kmeans))

# Format results as a DataFrame
Myresults = pd.DataFrame([df_cv.index,labels]).T
print(Myresults)


print(df_cv)
print(df_cv["child"]) 
x=df_cv["bad"]  ## col 6  
y=df_cv["help"]    ## col 29
z=df_cv["technology"]  ## col 74
colnames=df_cv.columns
print(colnames)

fig1 = plt.figure(figsize=(12, 12))
ax1 = Axes3D(fig1, rect=[0, 0, .90, 1], elev=48, azim=134)

ax1.scatter(x,y,z, cmap="RdYlGn", edgecolor='k', s=200,c=prediction_kmeans)
ax1.w_xaxis.set_ticklabels([])
ax1.w_yaxis.set_ticklabels([])
ax1.w_zaxis.set_ticklabels([])

ax1.set_xlabel('bad', fontsize=25)
ax1.set_ylabel('help', fontsize=25)
ax1.set_zlabel('technology', fontsize=25)
#plt.show()

df_cv.columns.get_loc("technology")

centers = kmeans_object_Count.cluster_centers_
print(centers)
#print(centers)
C1=centers[0,(6,29,74)]
print(C1)
C2=centers[1,(6,29,74)]
C3=centers[2,(6,29,74)]
print(C2)
xs=C1[0],C2[0],C3[0]
print(xs)
ys=C1[1],C2[1],C3[1]
zs=C1[2],C2[2],C3[2]


ax1.scatter(xs,ys,zs, c='black', s=2000, alpha=0.2)
plt.show()



#Checking sihlouette scores for clusters 2-11

# remember, anything past 15 looked really good based on the inertia
possible_K_values = [i for i in range(2,11)]

# we start with 1, as we can not have 0 clusters in k means
# iterate through each of our values
for each_value in possible_K_values:
    
    # iterate through, taking each value from 
    model = KMeans(n_clusters=each_value, init='k-means++',random_state=32)
    
    # fit it
    model.fit(df_cv)
    
    # find each silhouette score
    silhouette_score_individual = silhouette_samples(df_cv, model.predict(df_cv))

    print("Silhouette Score for ",each_value,"\n",silhouette_score(df_cv, model.predict(df_cv)))
            
    
    
    
kmeans_object_Count = KMeans(n_clusters=2)
#print(kmeans_object)
k_fit = kmeans_object_Count.fit(df_cv)


labels = kmeans_object_Count.labels_
prediction_kmeans = kmeans_object_Count.predict(df_cv)
#print(labels)
print(prediction_kmeans)

print("Silhouette Score for k = 2\n",silhouette_score(df_cv, prediction_kmeans))

# Format results as a DataFrame
Myresults = pd.DataFrame([df_cv.index,labels]).T
print(Myresults)


print(df_cv)
print(df_cv["child"]) 
x=df_cv["bad"]  ## col 6  
y=df_cv["help"]    ## col 29
z=df_cv["technology"]  ## col 74
colnames=df_cv.columns
print(colnames)

fig1 = plt.figure(figsize=(12, 12))
ax1 = Axes3D(fig1, rect=[0, 0, .90, 1], elev=48, azim=134)

ax1.scatter(x,y,z, cmap="RdYlGn", edgecolor='k', s=200,c=prediction_kmeans)
ax1.w_xaxis.set_ticklabels([])
ax1.w_yaxis.set_ticklabels([])
ax1.w_zaxis.set_ticklabels([])

ax1.set_xlabel('bad', fontsize=25)
ax1.set_ylabel('help', fontsize=25)
ax1.set_zlabel('technology', fontsize=25)
#plt.show()

df_cv.columns.get_loc("technology")

centers = kmeans_object_Count.cluster_centers_
print(centers)
#print(centers)
C1=centers[0,(6,29,74)]
print(C1)
C2=centers[1,(6,29,74)]
print(C2)
xs=C1[0],C2[0]
print(xs)
ys=C1[1],C2[1]
zs=C1[2],C2[2]


ax1.scatter(xs,ys,zs, c='black', s=2000, alpha=0.2)
plt.show()




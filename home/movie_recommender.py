import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import urllib.request
import pickle
import requests
import os


def look_for(m):
	m = m.lower()
	try:
		data.head()
		similarity.shape
	except:
		data, similarity = create_similarity()
	if m not in data['movie_title'].unique():
		return False
	return True

def create_similarity():
	file_dir = os.path.join(os.path.dirname(__file__), 'main_data.csv')
	data = pd.read_csv(file_dir)
    # creating a count matrix
	cv = CountVectorizer()
	count_matrix = cv.fit_transform(data['comb'])
    # creating a similarity score matrix
	similarity = cosine_similarity(count_matrix)
	return data,similarity

def rcmd(m):
    m = m.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
    if m not in data['movie_title'].unique():
        return('Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies')
    else:
        i = data.loc[data['movie_title']==m].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11] # excluding first item since it is the requested movie itself
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movie_title'][a])
        return l

# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["','')
    my_list[-1] = my_list[-1].replace('"]','')
    return my_list

def get_suggestions():
    data = pd.read_csv('main_data.csv')
    return list(data['movie_title'].str.capitalize())
import pandas as pd
import numpy as np
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
def combine_features(row):
	try:
		return row["keywords"] +" "+row["cast"]+" "+row["genres"]+" "+row["director"]
	except:
		print("Error:",row)
	
df= pd.read_csv("movie_dataset.csv")
features = ["keywords","cast","genres","director"]

for feature in features:
	df[feature]=df[feature].fillna(" ")
df["combined_features"]=df.apply(combine_features,axis=1)
cv=CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim =cosine_similarity(count_matrix)  
movie_user_likes = input("Enter a movie you like:\n")

movie_index=get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies= sorted(similar_movies,key=lambda x:x[1],reverse=True)

try:
	i=0
	
	print("\nYou might also like:")
	for movie in sorted_similar_movies:
		
		print(get_title_from_index(movie[0]))
		time.sleep(0.5)
		i=i+1
		if i>15:
			break
except:
	print(movie_user_likes,"is not in the dataset")
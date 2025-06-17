import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies.csv")

count_vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|')) #sayiya cevir
genre_matrix = count_vectorizer.fit_transform(df['genres'])  # 0,1 

cosine_sim = cosine_similarity(genre_matrix) #Vektörler arasındaki benzerliği ölç
#sinus- difference olcer
#cosinus- similarity olcer

def recommend(movie_title, top_n=3):
    if movie_title not in df['title'].values:  #key-> title ve genre
        print("Film bulunamadı.")
        return
    index = df[df['title'] == movie_title].index[0] #kacinci sirada
    similar_scores = list(enumerate(cosine_sim[index]))
    similar_scores = sorted(similar_scores, key=lambda x: x[1], reverse=True)
    similar_movies = [df.iloc[i[0]]['title'] for i in similar_scores[1:top_n+1]]
    print(f"\n '{movie_title}' için önerilen filmler:")
    for movie in similar_movies:
        print("->", movie)

movie_name = input("Please enter your favorite movie: ")
recommend(movie_name)


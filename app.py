import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies.csv")

count_vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|'))
genre_matrix = count_vectorizer.fit_transform(df['genres'])
cosine_sim = cosine_similarity(genre_matrix)

def recommend(movie_title, top_n=3):
    if movie_title not in df['title'].values:
        return ["Film bulunamadı."]
    index = df[df['title'] == movie_title].index[0]
    similar_scores = list(enumerate(cosine_sim[index]))
    similar_scores = sorted(similar_scores, key=lambda x: x[1], reverse=True)
    similar_movies = [df.iloc[i[0]]['title'] for i in similar_scores[1:top_n+1]]
    return similar_movies

st.title("🎬 Movie Recommender System")

user_input = st.text_input("Bir film adı girin:")

if user_input:
    st.subheader(f"🎯 '{user_input}' için önerilen filmler:")
    for movie in recommend(user_input):
        st.write("👉", movie)

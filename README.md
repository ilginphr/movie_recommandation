# 🎬 Movie Recommendation System

This is a simple **content-based movie recommender system** built with Python and deployed using **Streamlit**.  
It suggests similar movies based on **genre similarity** using `CountVectorizer` and `cosine similarity`.

---

## 📌 Features

- Takes a movie title from user input
- Recommends similar movies based on shared genres
- Built with pandas, scikit-learn, and Streamlit
- Easy-to-use web interface

---

## 🚀 How It Works

1. **Preprocessing genres** using `CountVectorizer`
2. **Computing similarity** between movies with `cosine_similarity`
3. User inputs a movie title
4. Top N similar movies are returned based on genre similarity

---

## 🛠️ Technologies Used

- Python 🐍
- pandas
- scikit-learn
- Streamlit
- Git & GitHub

---

## 🖥️ Demo

You can run the app locally using:

```bash
streamlit run app.py

# 🎬 Movie Recommender System

A simple **content-based movie recommendation system** that suggests similar films based on genres. Built using Python, pandas, and scikit-learn.

## 📌 Project Overview

This project takes a movie title as input and recommends similar movies based on their genre similarity. It uses **CountVectorizer** and **cosine similarity** to calculate how close each movie is to the selected one.

## 📁 Dataset

The dataset (`movies.csv`) contains movie titles and their genres. Example:

| Title            | Genres                  |
|------------------|--------------------------|
| The Matrix       | Action\|Sci-Fi           |
| Inception        | Action\|Sci-Fi\|Thriller |
| Titanic          | Romance\|Drama           |

## ⚙️ How It Works

1. Reads the dataset using pandas.
2. Encodes genres using `CountVectorizer`.
3. Calculates similarity using `cosine_similarity`.
4. Recommends top N most similar movies.

## ▶️ How to Run

```bash
python recommender.py

# 🎬 Content-Based Movie Recommendation System

## 📌 Demo

Click on the Live Demo:

> 🔗 [Live Demo](https://movie-recommendation-system-py.streamlit.app/)

---

This project is a **Content-Based Movie Recommendation System** developed using the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). It suggests movies based on user preferences by analyzing movie metadata such as storyline, genre, director, and cast using Natural Language Processing techniques.

## 📌 Project Objective

* Recommend similar movies using content-based filtering.
* Use Bag of Words (BoW) for text feature extraction.
* Compute similarity using cosine similarity.
* Deliver recommendations via an interactive **Streamlit** web application.

## 📁 Dataset

* **Source:** [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* **Contents:**

  * Title
  * Genres
  * Overview (Storyline)
  * Director
  * Cast
  * Other

## 🛠️ Tech Stack

| Component      | Tools Used                                   |
| -------------- | -------------------------------------------- |
| Programming    | Python                                       |
| Libraries      | Pandas, NumPy, Scikit-learn, NLTK, Streamlit |
| NLP Techniques | Bag of Words (BoW), Text Preprocessing       |
| Deployment     | Streamlit Cloud

## 🔄 Project Pipeline

1. **Data Collection** – TMDB 5000 dataset from Kaggle
2. **Data Cleaning & Preprocessing** – Handle nulls, extract features
3. **Feature Engineering** – Combine important text features
4. **Vectorization** – Bag of Words model for converting text to vectors
5. **Similarity Calculation** – Cosine Similarity
6. **Recommendation Logic** – Get top N similar movies
7. **Web Interface** – Built using Streamlit for user interaction
8. **Deployment** – To be hosted for public/institutional access

## 🧹 Preprocessing Steps

* Handle missing values in relevant columns
* Merge textual features (e.g., storyline, genre, director)
* Remove stopwords and apply lowercase transformations
* Vectorize using `CountVectorizer` (BoW model)

## 🚀 How to Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/HarisKhann1/Movie-Recommendation-System.git
   cd movie-recommendation-system
   ```

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## 🤝 Acknowledgments

* TMDB for providing the dataset
* Scikit-learn & NLTK for powerful ML and NLP tools
* Streamlit for enabling quick app deployment


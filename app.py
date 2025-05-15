import streamlit as st
import pickle
import requests

# Load the movies list in binary mode
movies_list = pickle.load(open('./movies.pkl', 'rb'))
movies_list_title = movies_list["title"].values

# Load the similarity matrix in binary mode
similarity = pickle.load(open('./similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies_list[movies_list["title"] == movie].index[0] # index of the given movie
    distances = similarity[movie_index] # get all the movies that is similar to the given movie (distances)
    rec_movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:7] # get the most five similar movies

    rec_movie_id =  [movies_list.iloc[i[0]]["movie_id"] for i in rec_movies_list]
    rec_movie_title =  [movies_list.iloc[i[0]]["title"] for i in rec_movies_list]

    rec_movie_poster = []
    for i in rec_movie_id:
        rec_movie_poster.append(fetch_poster(i))

    return rec_movie_title, rec_movie_poster


def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data = response.json()
    overview = data['overview']
    return  "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# ------------------------------------------------------------------------

st.title("Movie Recommendation System") 
# select box to select movie name
selected_movie_name = st.selectbox(
    "Select a movie",
    movies_list_title,
)   


if st.button("Recommend"):
    # add a top margin of 50px
    st.markdown("<style>{ margin-top: 100px; }</style>", unsafe_allow_html=True)
    
    rec_movie_title, rec_movie_poster = recommend(selected_movie_name)
    # First row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(rec_movie_poster[0])
        st.text(rec_movie_title[0])
    with col2:
        st.image(rec_movie_poster[1])
        st.text(rec_movie_title[1])
    with col3:
        st.image(rec_movie_poster[2])
        st.text(rec_movie_title[2])

    st.markdown("<br>", unsafe_allow_html=True)  # Add gap between rows

    # Second row
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(rec_movie_poster[3])
        st.text(rec_movie_title[3])
    with col5:
        st.image(rec_movie_poster[4])
        st.text(rec_movie_title[4])
    with col6:
        st.image(rec_movie_poster[5])
        st.text(rec_movie_title[5])
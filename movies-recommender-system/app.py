import streamlit as st # type: ignore
import pickle
import requests
import pandas as pd


def fetch_poster (movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=455d020b52aa5a4d6548ee0071d39301&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    
    return full_path
    
    
def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])

    recommended_movies = []
    recommended_movies_posters = []
    
    for i in movies_list[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        # movies title
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_movies_posters


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.header('Movie Recommender System')

movie_list = movies['title'].values

selected_movie_name = st.selectbox(
    'Which movie you recently watched?',
    movie_list
)



if st.button('Recommend'):
    recommendations_name, posters = recommend(selected_movie_name)
    
    cols = st.columns(5)
    
    for i, col in enumerate(cols):
        with col:
            st.text(recommendations_name[i])
            st.image(posters[i])
    
        
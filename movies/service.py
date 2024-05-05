import streamlit as st
from movies.repository import MovieRepository


class MovieService:
    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        if 'movie' in st.session_state:
            return st.session_state.movie
        movie = self.movie_repository.get_movies()
        st.session_state.movie = movie
        return movie

    def create_movies(self, title, release_date, genre, actors, resume):
        movies = dict(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            resume=resume,
        )
        new_movie = self.movie_repository.create_movie(movies)
        st.session_state.movie.append(new_movie)
        return new_movie

    def get_movie_stats(self):
        return self.movie_repository.get_movies_stats()

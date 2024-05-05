import streamlit as st
from genres.repository import GenreRepository


class GenreService:

    def __init__(self):
        self.genre_repository = GenreRepository()

    def get_genres(self):
        if 'genre' in st.session_state:
            return st.session_state.genre
        genre = self.genre_repository.get_genres()
        st.session_state.genres = genre
        return genre

    def create_genre(self, name):
        genre = dict(
            name=name,
        )
        new_genre = self.genre_repository.create_genre(genre)
        st.session_state.genre.append(new_genre)
        return new_genre

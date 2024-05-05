import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from movies.service import MovieService
from genres.service import GenreService
from actors.service import ActorService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de Filmes')

        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])

        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme encontrado')

    st.title('Cadastrar novo Filme')

    title = st.text_input('Titulo')
    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genres_name = {genre['name']: genre['id'] for genre in genres}
    select_genre_name = st.selectbox('Gênero', list(genres_name.keys()))   # type: ignore

    actor_service = ActorService()
    actors = actor_service.get_actor()
    actor_name = {actor['name']: actor['id'] for actor in actors}  # type: ignore

    selected_actors_names = st.multiselect(
        'Atores/Atrizes', list(actor_name.keys())
    )
    selected_actors_id = {actor_name[name] for name in selected_actors_names}

    resume = st.text_area('Resumo')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movies(
            title=title,
            release_date=release_date,
            genre=genres_name[select_genre_name],
            actors=selected_actors_id,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o filme, verifique os campos')

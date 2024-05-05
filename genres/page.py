import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService

# genres = [
#     {'id': 1, 'name': 'Ação'},
#     {'id': 2, 'name': 'Comedia'},
#     {'id': 3, 'name': 'Terror'},
# ]


def show_genre():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de genres')
        # altera o formato de json para transformar em um dataframe para o pandas ler # noqa
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=pd.DataFrame(genres_df),
            reload_data=True,
            key='genres_grid',
        )
    else:
        st.warning('Nenhum gênero encontrado')

    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do Gênero')

    if st.button('Cadastrar'):
        create_genre = genre_service.create_genre(name)
        if create_genre is not None:
            st.rerun()
        else:
            st.error('Erro ao cadastrar gênero, Verifique os campos')

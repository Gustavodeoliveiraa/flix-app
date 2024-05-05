import pandas as pd
from datetime import datetime
import streamlit as st
from st_aggrid import AgGrid
from actors.service import ActorService

actors = [
    {'id': 1, 'name': 'Leonardo Di Caprio'},
    {'id': 2, 'name': 'Chris Rocl'},
    {'id': 3, 'name': 'Will Smith'},
]


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actor()

    if actors:
        actors_df = pd.json_normalize(actors)
        st.write('Lista de Atores')

        AgGrid(
            data=pd.DataFrame(actors_df),
            reload_data=True,
            key='actors_grid',
        )
    else:
        st.warning('Nenhum Ator/Atriz encontrado')

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    birthday = st.date_input(
        label='Data de nascimento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )

    nationality_dropdown = ['BRAZIL', 'USA']

    nationality = st.selectbox(
        label='nationality',
        options=nationality_dropdown
    )

    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name, birthday=birthday, nationality=nationality
        )

        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o(a) Ator/Atriz. Verifique os campos')

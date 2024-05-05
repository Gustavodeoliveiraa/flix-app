import streamlit as st
from genres.page import show_genre
from actors.page import show_actors
from home.page import show_home
from login.page import show_login
from movies.page import show_movies
from reviews.page import show_review


def main():
    if 'token' not in st.session_state:
        show_login()
    else:

        st.title('Flix App')

        menu_option = st.sidebar.selectbox(
            'Selecione uma opção abaixo',
            ['Inicio', 'Gêneros', 'Atore/Atrizes', 'Filmes', 'Avaliações']
        )

        match menu_option:
            case 'Inicio':
                show_home()

            case 'Gêneros':
                st.write('Gêneros')
                show_genre()

            case 'Atore/Atrizes':
                st.write('Atrizes')
                show_actors()

            case 'Filmes':
                st.write('Filmes')
                show_movies()

            case 'Avaliações':
                st.write('Avaliações')
                show_review()


if __name__ == '__main__':
    main()

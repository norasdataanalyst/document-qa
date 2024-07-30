import streamlit as st
import pandas as pd
import os

# Lecture des données de comptes depuis un fichier CSV
file_path = 'comptes.csv'
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    st.error(f"Le fichier {file_path} n'existe pas.")

# Vérifiez et renommez les colonnes si nécessaire
expected_columns = ['name', 'password', 'email', 'failed_login_attempts', 'logged_in', 'role']
if list(df.columns) != expected_columns:
    df.columns = expected_columns

# Page d'authentification
def authentification():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = df[(df['name'] == username) & (df['password'] == password)]
        if not user.empty:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.experimental_set_query_params(logged_in=True)  # Déclenche un rerun en modifiant les paramètres de la requête
        else:
            st.error("Les champs username et mot de passe doivent être remplis")

        # Page d'accueil
        def accueil():
            st.title("Bienvenue sur ma page")
            st.image("https://media.giphy.com/media/3o6ZsXhV7vG9U7mGDe/giphy.gif", use_column_width=True)
        
        # Page de photos de chat
        def photos_chat():
            st.title("Bienvenue dans l'album de mon chat 😺")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image("https://static.streamlit.io/examples/cat.jpg")
            with col2:
                st.image("https://static.streamlit.io/examples/dog.jpg")
            with col3:
                st.image("https://static.streamlit.io/examples/owl.jpg")
        
        # Menu dans la sidebar
        def menu():
            with st.sidebar:
                if st.button("Déconnexion"):
                    st.session_state['logged_in'] = False
                    st.session_state['username'] = None
                    st.experimental_set_query_params(logged_in=False)  # Déclenche un rerun en modifiant les paramètres de la requête
                st.write(f"Bienvenue {st.session_state['username']}")
                selection = st.radio("Navigation", ["Accueil", "Les photos de mon chat"])
                if selection == "Accueil":
                    accueil()
                elif selection == "Les photos de mon chat":
                    photos_chat()
        
        # Main
        if 'logged_in' not in st.session_state:
            st.session_state['logged_in'] = False
        
        query_params = st.experimental_get_query_params()
        if 'logged_in' in query_params:
            st.session_state['logged_in'] = query_params['logged_in'][0] == 'True'
        
        if st.session_state['logged_in']:
            menu()
        else:
            authentification()

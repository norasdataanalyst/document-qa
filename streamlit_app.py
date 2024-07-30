import streamlit as st
import pandas as pd

# Lecture des données de comptes depuis un fichier CSV
df = pd.read_csv('comptes.csv')

# Page d'authentification
def authentification():
    st.title("Page d'authentification")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        user = df[(df['name'] == username) & (df['password'] == password)]
        if not user.empty:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect")

# Page d'accueil
def accueil():
    st.title(f"Bienvenue {st.session_state['username']}!")
    st.write("Voici l'album de photos de mon chat :")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Chat 1")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.header("Chat 2")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col3:
        st.header("Chat 3")
        st.image("https://static.streamlit.io/examples/cat.jpg")

# Menu dans la sidebar
def menu():
    with st.sidebar:
        st.write(f"Bienvenue {st.session_state['username']}")
        if st.button("Déconnexion"):
            st.session_state['logged_in'] = False

# Main
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    menu()
    accueil()
else:
    authentification()

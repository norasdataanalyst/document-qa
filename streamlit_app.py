import streamlit as st
import pandas as pd
import os

# Lecture des données de comptes depuis un fichier CSV
file_path = 'comptes.csv'
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    st.error(f"Le fichier {file_path} n'existe pas.")
    st.stop()

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
        if username and password:
            user = df[(df['name'] == username) & (df['password'] == password)]
            if not user.empty:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.experimental_rerun()
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect")
        else:
            st.error("Les champs username et mot de passe doivent être remplis")

# Page d'accueil
def accueil():
    st.title("Accueil")
    st.write("Bienvenue sur la page d'accueil!")
    st.image("https://media.giphy.com/media/5yLgocuQi3aB8lDO9S8/giphy.gif")

# Page de photos de chat
def photos_chat():
    st.title("Bienvenue dans l'album de mes animaux 😺")
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
        st.write(f"Bienvenue *{st.session_state['username']}*")
        if st.button("Déconnexion"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = None
            st.experimental_rerun()
        
        selection = st.radio("Navigation", ["Accueil", "Les photos de mon chat"], index=0, key="menu")
    
    if selection == "Accueil":
        accueil()
    elif selection == "Les photos de mon chat":
        photos_chat()

# Main
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    menu()
else:
    authentification()

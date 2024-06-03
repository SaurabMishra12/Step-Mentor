import streamlit as st
import app

users={"Saurab":"thisispass", "Shubham":"thisispass"}

def login(username,password):
    if username in users and users[username] == password:
        return True
    else:
        return False





    st.title("Welcome to **Step Mentor**")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        if login(username, password):
            st.success("Login successful!")
            st.set_query_params(page="app")
        else:
            st.error("Invalid username or password")






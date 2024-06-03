import streamlit as st
import Credential
import app

def main():
    query_params = st.experimental_get_query_params()
    page = query_params.get("page", ["login"])[0]

    if page == "app":
        app.main()
    else:
        credential.main()

if __name__ == "__main__":
    main()

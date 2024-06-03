import time
import streamlit as st

def start_timer():
    st.session_state.start_time = time.time()
    st.session_state.remaining_time = 10*60


def display_timer():
    remaining_time =int(st.session_state.remaining_time)
    minutes, seconds = divmod(remaining_time, 60)
    st.write(f"Time:{minutes:02d}:{seconds:02d}")
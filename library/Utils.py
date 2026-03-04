import streamlit as st
import time
from library import Statemanagment
import pandas as pd

def play_sound():
    with open("resources/sound.mp3", "rb") as audio_file: audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)
    time.sleep(2)
    st.rerun()


def display_arrows(side, difficulty):
    col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
    if side == 'left':
        with col3: st.image("resources/left.png")
        if difficulty < 3:
            with col2: st.image("resources/left.png")
        if difficulty < 2:
            with col1: st.image("resources/left.png")
    if side == 'right':
        with col4: st.image("resources/right.png")
        if difficulty < 3:
            with col5: st.image("resources/right.png")
        if difficulty < 2:
            with col6: st.image("resources/right.png")


def update_difficulty_and_trial(correct):
    difficulty = Statemanagment.get_state('difficulty')
    if correct: difficulty = difficulty + 1
    else: difficulty = difficulty - 1
    if difficulty < 1: difficulty = 1
    if difficulty > 3: difficulty = 3
    Statemanagment.update_state('difficulty', difficulty)
    trial = Statemanagment.get_state('trial')
    Statemanagment.update_state('trial', trial)
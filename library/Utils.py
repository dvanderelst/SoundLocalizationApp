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
    col1, col2 = st.columns([1, 1])
    multiplier = 4 - difficulty
    if side == 'left': st.header('⬅️'* multiplier, text_alignment='center', width='stretch')
    if side == 'right': st.header('➡️' * multiplier, text_alignment='center', width='stretch')



def update_difficulty_and_trial(correct):
    difficulty = Statemanagment.get_state('difficulty')
    if correct: difficulty = difficulty + 1
    else: difficulty = difficulty - 1
    if difficulty < 1: difficulty = 1
    if difficulty > 3: difficulty = 3
    Statemanagment.update_state('difficulty', difficulty)
    Statemanagment.increment_state('trial', 1)
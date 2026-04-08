import streamlit as st
import time
import base64
from library import Statemanagment
import pandas as pd


def get_image_base64(image_path):
    """Convert image to base64 for HTML embedding"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


def show_centered_feedback(feedback_text, correct, correct_image="resources/correct.png", incorrect_image="resources/incorrect.png"):
    """Display centered feedback with text and image"""
    # Add CSS for centering
    st.markdown("""
    <style>
    .centered-feedback {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin: 20px auto;
        width: 100%;
    }
    .feedback-text {
        font-size: 24px;
        margin-bottom: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Show centered content
    image_path = correct_image if correct else incorrect_image
    image_base64 = get_image_base64(image_path)
    
    st.markdown(f"""
    <div class="centered-feedback">
        <p class="feedback-text">{feedback_text}</p>
        <img src="data:image/png;base64,{image_base64}" width="200">
    </div>
    """, unsafe_allow_html=True)

def play_sound():
    with open("resources/sound.wav", "rb") as audio_file: audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/wav", autoplay=True)
    time.sleep(2)
    st.rerun()


def display_arrows(side, difficulty):
    col1, col2 = st.columns([1, 1])
    multiplier = 4 - difficulty
    if side == 'left': st.header('⬅️'* multiplier, text_alignment='center', width='stretch')
    if side == 'right': st.header('➡️' * multiplier, text_alignment='center', width='stretch')

def display_diagram(side, difficulty):
    image = 'resources/center.png'
    if side == 'left': image = f'resources/level{difficulty}L.png'
    if side == 'right': image = f'resources/level{difficulty}R.png'
    st.image(image, width='stretch')


def update_difficulty_and_trial(correct):
    difficulty = Statemanagment.get_state('difficulty')
    if correct: difficulty = difficulty + 1
    else: difficulty = difficulty - 1
    if difficulty < 1: difficulty = 1
    if difficulty > 3: difficulty = 3
    Statemanagment.update_state('difficulty', difficulty)
    Statemanagment.increment_state('trial', 1)
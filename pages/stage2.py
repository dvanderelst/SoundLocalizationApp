import streamlit as st
from library import Statemanagment
from library import Utils
import random

side = random.choice(['left', 'right'])
Statemanagment.update_state('side', side, condition='if_none')

sound_was_played = Statemanagment.get_state('sound_played') > 0

difficulty = Statemanagment.get_state('difficulty')
side = Statemanagment.get_state('side')

st.header('Step 2: speaker at side', text_alignment='center')
st.text(f'Place the speaker on the {side} at difficulty {difficulty} and play the sound once', text_alignment='center', width='stretch')
Utils.display_arrows(side, difficulty)
play = st.button('Play sound', width='stretch')
confirm = st.button("Next", width='stretch', disabled= not sound_was_played)

if play:
    Statemanagment.increment_state('sound_played')
    Utils.play_sound()

if confirm:
    Statemanagment.update_state('sound_played', 0)
    st.switch_page('pages/stage3.py')




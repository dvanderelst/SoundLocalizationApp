import streamlit as st
from library import Statemanagment
from library import Utils

trial = Statemanagment.get_state('trial')
number_of_trials = Statemanagment.get_state('number_of_trials')
sound_was_played = Statemanagment.get_state('sound_played') > 0

st.header('Step 1: speaker at center', text_alignment='center')
st.text(f'Trial {trial} of {number_of_trials}', text_alignment='center', width='stretch')
st.text('Place the speaker in the center and play the sound once.', text_alignment='center', width='stretch')
play = st.button('Play sound', width='stretch')
confirm = st.button("Next", width='stretch', disabled= not sound_was_played)

if play:
    Statemanagment.increment_state('sound_played')
    Utils.play_sound()

if confirm:
    Statemanagment.update_state('sound_played', 0)
    st.switch_page('pages/stage2.py')


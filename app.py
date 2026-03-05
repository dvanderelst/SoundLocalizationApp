import streamlit as st
from library import Statemanagment

variables = {}



variables['trial'] = 0
variables['side'] = None
variables['difficulty'] = 1
variables['participant'] = None
variables['sound_played'] = 0
variables['condition'] = None
variables['number_of_trials'] = 3

variables['trial_history'] = []
variables['difficulty_history'] = []
variables['side_history'] = []
variables['response_history'] = []
variables['correct_history'] = []

Statemanagment.init_state(variables)

with st.form("settings_form"):
    participant = st.text_input("Participant name:")
    condition = st.radio("Condition:", ("Real ears", "Artificial ears"))
    if st.form_submit_button("Start"):
        Statemanagment.update_state('participant', participant)
        Statemanagment.update_state('condition', condition)
        Statemanagment.update_state('trial', 1)
        st.switch_page('pages/stage1.py')



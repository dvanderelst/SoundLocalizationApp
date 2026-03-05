import streamlit as st
from library import Statemanagment
from library import Utils
import time

st.header('Step 1: Record response', text_alignment='center')
options = ['Left', 'Right']
label = 'What was the pariticipants response?'
response = st.segmented_control(label, options, selection_mode='single', width='stretch')
confirm = st.button("Confirm", width='stretch')

if confirm and response:
    # Store current trial data
    correct  = response.lower() == Statemanagment.get_state('side')
    feedback = 'Correct!' if correct else 'Incorrect!'
    if correct: st.header('😄 ' + feedback)
    if not correct: st.header('😭 ' + feedback)
    time.sleep(2)

    correct = str(correct)
    Statemanagment.append_state('trial_history', other_key='trial')
    Statemanagment.append_state('difficulty_history', other_key='difficulty')
    Statemanagment.append_state('side_history', other_key='side')
    Statemanagment.append_state('response_history', response)
    Statemanagment.append_state('correct_history', correct)


    # check whether we should end things
    trial = Statemanagment.get_state('trial')
    number_of_trials = Statemanagment.get_state('number_of_trials')
    if trial == number_of_trials: st.switch_page('pages/final.py')

    # prepare next trials and switch page
    Utils.update_difficulty_and_trial(correct)
    Statemanagment.update_state('side', None) # This allows the next iteration to select a new random side
    st.switch_page('pages/stage1.py')

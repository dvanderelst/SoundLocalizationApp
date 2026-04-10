import streamlit as st
from library import Statemanagment
from library import Utils

participant = Statemanagment.get_state('participant')

st.header('Step 3: Record response', text_alignment='center')
st.text(f'Ask {participant} to respond which side the speaker was moved to.', text_alignment='center')

# Guard: redirect to stage2 if side hasn't been set yet (e.g. direct navigation)
if Statemanagment.get_state('side') is None:
    st.switch_page('pages/stage2.py')

response = None
st.image('resources/pointing.png', width='stretch')
options = ["Right!", "Left!"]
trial_key = f'response_{Statemanagment.get_state("trial")}'
selection_label = st.segmented_control('Response', options, key=trial_key, width='stretch', label_visibility='hidden')
if selection_label and 'right' in selection_label: response = 'right'
if selection_label and 'left' in selection_label: response = 'left'

# Confirmation button (only enabled once a selection is made)
confirm = st.button("Confirm Selection", disabled=response is None, use_container_width=True)
if confirm:
    correct = response.lower() == Statemanagment.get_state('side')

    Statemanagment.append_state('trial_history', other_key='trial')
    Statemanagment.append_state('difficulty_history', other_key='difficulty')
    Statemanagment.append_state('side_history', other_key='side')
    Statemanagment.append_state('response_history', response)
    Statemanagment.append_state('correct_history', str(correct))

    trial = Statemanagment.get_state('trial')
    number_of_trials = Statemanagment.get_state('number_of_trials')

    if trial == number_of_trials:
        next_page = 'pages/final.py'
    else:
        Utils.update_difficulty_and_trial(correct)
        Statemanagment.update_state('side', None)
        next_page = 'pages/stage1.py'

    st.session_state.temp_selection = None
    st.session_state.feedback_text = f'{participant} responded correctly' if correct else f'{participant} responded incorrectly'
    st.session_state.feedback_correct = correct
    st.session_state.next_page = next_page
    st.switch_page('pages/feedback.py')

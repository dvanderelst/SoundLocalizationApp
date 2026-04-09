import streamlit as st
from library import Statemanagment
from library import Utils

participant = Statemanagment.get_state('participant')

st.header('Step 3: Record response', text_alignment='center')
st.text(f'Ask {participant} to respond which side the speaker was moved to.')
label = f"What was {participant}'s response?"

# Initialize response variable at the top
response = None

st.markdown(f"<h3 style='text-align: center; margin-bottom: 20px;'>{label}</h3>", unsafe_allow_html=True)

if 'temp_selection' not in st.session_state:
    st.session_state.temp_selection = None

st.markdown("""
<style>
[data-testid="stHorizontalBlock"] {
    flex-wrap: nowrap !important;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image('resources/point_left.png', use_container_width=True)
with col2:
    st.image('resources/point_right.png', use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("Speaker was moved to left!", use_container_width=True, key="btn_left",
                 type="primary" if st.session_state.temp_selection == 'Left' else "secondary"):
        st.session_state.temp_selection = 'Left'
        st.rerun()
with col2:
    if st.button("Speaker was moved to right!", use_container_width=True, key="btn_right",
                 type="primary" if st.session_state.temp_selection == 'Right' else "secondary"):
        st.session_state.temp_selection = 'Right'
        st.rerun()

temp_selection = st.session_state.temp_selection

# Confirmation button (only enabled once a selection is made)
confirm = st.button("Confirm Selection", disabled=temp_selection is None, use_container_width=True)

if confirm and temp_selection:
    response = temp_selection

if response:
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

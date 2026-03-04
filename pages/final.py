import streamlit as st
from library import Statemanagment
from library import Utils

selected_variables = ['trial_history', 'difficulty_history', 'side_history', 'response_history', 'correct_history']
dataframe = Statemanagment.build_dataframe(selected_variables)
participant = Statemanagment.get_state('participant')
condition = Statemanagment.get_state('condition')
dataframe['participant'] = participant
dataframe['condition'] = condition

st.header('Final Results')
st.dataframe(dataframe)
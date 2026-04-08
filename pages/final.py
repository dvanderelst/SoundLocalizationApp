import streamlit as st
from library import Statemanagment

selected_variables = ['trial_history', 'difficulty_history', 'side_history', 'response_history', 'correct_history']
dataframe = Statemanagment.build_dataframe(selected_variables)
participant = Statemanagment.get_state('participant')
condition = Statemanagment.get_state('condition')
dataframe['participant'] = participant
dataframe['condition'] = condition

st.header('Final Results')
st.dataframe(dataframe)

csv = dataframe.to_csv(index=False)
st.download_button("Download CSV", data=csv, file_name=f"{participant}_{condition}.csv", mime="text/csv", use_container_width=True)

if st.button("Start new session", use_container_width=True):
    Statemanagment.reset_state()
    st.switch_page('app.py')
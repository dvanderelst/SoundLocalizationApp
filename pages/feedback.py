import streamlit as st
from library import Utils

feedback_text = st.session_state.get('feedback_text', '')
correct = st.session_state.get('feedback_correct', False)
next_page = st.session_state.get('next_page', 'pages/stage1.py')

st.header('Feedback', text_alignment='center')
Utils.show_centered_feedback(feedback_text, correct)

if st.button("OK", use_container_width=True):
    st.switch_page(next_page)

import uuid
import streamlit as st
from library import Statemanagment
from library import Database

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

st.divider()

# --- Database commit flow ---
if 'committed' not in st.session_state:
    st.session_state.committed = False
if 'show_commit_form' not in st.session_state:
    st.session_state.show_commit_form = False

if st.session_state.committed:
    st.success(f"Data committed to database (run ID: `{st.session_state.run_id}`)")

elif st.session_state.show_commit_form:
    if 'submitting' not in st.session_state:
        st.session_state.submitting = False

    comment = st.text_area("Comment (optional):", key='db_comment', disabled=st.session_state.submitting)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Submit", use_container_width=True, type="primary", disabled=st.session_state.submitting):
            st.session_state.submitting = True
            st.rerun()
    with col2:
        if st.button("Cancel", use_container_width=True, disabled=st.session_state.submitting):
            st.session_state.show_commit_form = False
            st.rerun()

    if st.session_state.get('commit_error'):
        st.error(f"Failed to commit: {st.session_state.commit_error}")
        st.session_state.commit_error = None

    if st.session_state.submitting:
        with st.spinner("Committing to database..."):
            run_id = str(uuid.uuid4())
            try:
                Database.commit_run(dataframe, run_id, st.session_state.db_comment)
                st.session_state.run_id = run_id
                st.session_state.committed = True
                st.session_state.show_commit_form = False
            except Exception as e:
                st.session_state.commit_error = str(e)
            finally:
                st.session_state.submitting = False
        st.rerun()

else:
    if st.button("Commit to database", use_container_width=True):
        st.session_state.show_commit_form = True
        st.rerun()

st.divider()

if st.button("Start new session", use_container_width=True):
    Statemanagment.reset_state()
    st.switch_page('app.py')

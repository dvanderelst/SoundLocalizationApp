import streamlit as st
import pandas

def init_state(initial_variables):
    keys = initial_variables.keys()
    for key in keys:
        if key not in st.session_state: st.session_state[key] = initial_variables[key]

def reset_state():
    for key in list(st.session_state.keys()): del st.session_state[key]

def print_state(to_console=True, to_gui=True):
    all_text = ''
    for key in list(st.session_state.keys()):
        value = st.session_state[key]
        text = f'{key}: {value}'
        all_text = all_text + '\n' + text
    if to_console: print(all_text)
    if to_gui: st.code(all_text)

def update_state(key, value, condition= 'always'):
    current_value = st.session_state[key]
    if condition == 'always':
        st.session_state[key] = value
        return
    if condition == 'if_none':
        if current_value is None: st.session_state[key] = value
        return
    if condition == 'if_not_none':
        if current_value is not None: st.session_state[key] = value
        return
    if condition == 'if_different':
        if current_value != value: st.session_state[key] = value
        return

def get_state(key):
    return st.session_state[key]

def append_state(key, value=None, other_key=None):
    if other_key is None:
        current = st.session_state[key]
        current.append(value)
        st.session_state[key] = current.copy()
    else:
        current = st.session_state[key]
        to_append = st.session_state[other_key]
        current.append(to_append)
        st.session_state[key] = current.copy()

def increment_state(key, value=1):
    current = st.session_state[key]
    new = current + value
    st.session_state[key] = new


def build_dataframe(variables):
    data = {}
    for variable in variables:
        values = get_state(variable)
        data[variable] = values
        print(values)
    data = pandas.DataFrame(data)
    return data


import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from main import *

st.set_page_config(initial_sidebar_state="collapsed",
                   page_title="Enter data",
                   page_icon="📑",
                   )

st.header("Please enter your desired data Resume and JD")

choose_type = load_title_dasboard()
if choose_type == 'CSV':
        Resumes, Jobs = load_input_data_Resumes(), load_input_data_Jobs()
else:
    Resumes, Jobs = load_input_data_Resumes_docx(), load_input_data_Jobs_docx()

session_state = st.session_state
session_state['Resumes'] = Resumes
session_state["Jobs"] = Jobs

next_page = st.button("Show Description Name and Information Job and Resumes")
if next_page:
    switch_page("show_description_name")
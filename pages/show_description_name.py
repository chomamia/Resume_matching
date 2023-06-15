import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from main import *
import asyncio

st.set_page_config(initial_sidebar_state="collapsed",
                   page_title="Show information",
                   page_icon="📑",
                   )

st.header("Show Description Name and Information Job and Resumes")
session_state = st.session_state
Resumes = session_state["Resumes"]
Jobs = session_state["Jobs"]

print(Resumes)
show_description_name(Jobs)
index  =  show_description(Jobs)
info_retrieval = show_information_retrieval(Jobs, index)
info_retrieval_resumes = show_information_retrieval_resumes(Resumes)
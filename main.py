import matplotlib.colors as mcolors
import gensim
import gensim.corpora as corpora
from operator import index
from wordcloud import WordCloud
from pandas._config.config import options
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import Similar
from PIL import Image
import time
from Job_resume_matching.extraction import extraction
from Job_resume_matching.matching import matching
from Distill import upload_file_jobs_csv, upload_file_resumes_csv, upload_file_Resumes_csv
import asyncio
# import nest_asycio


async def load_title_dasboard():
    image = Image.open('Images//logo.png')
    st.image(image, use_column_width=True)

    st.title("Resume Matcher")

async def load_input_data_Resumes():
    Resumes = upload_file_Resumes_csv()
    return Resumes

async def load_input_data_Jobs():
    Jobs = upload_file_jobs_csv()
    return Jobs

async def load_input_data_resumes():
    resumes = upload_file_resumes_csv()
    return resumes

async def show_description_name(Jobs):
    if len(Jobs['Name']) <= 1:
        st.write(
            "There is only 1 Job Description present. It will be used to create scores.")
    else:
        st.write("There are ", len(Jobs['Name']),
                "Job Descriptions available. Please select one.")
    # Asking to Print the Job Desciption Names
    if len(Jobs['Name']) > 1:
        option_yn = st.selectbox(
            "Show the Job Description Names?", options=['YES', 'NO'])
        if option_yn == 'YES':
            index = [a for a in range(len(Jobs['Name']))]
            fig = go.Figure(data=[go.Table(header=dict(values=["Job No.", "Job Desc. Name"], line_color='darkslategray',
                                                    fill_color='lightskyblue'),
                                        cells=dict(values=[index, Jobs['Name']], line_color='darkslategray',
                                                    fill_color='cyan'))
                                ])
            fig.update_layout(width=700, height=400)
            st.write(fig)

async def show_description(Jobs):
    # Asking to chose the Job Description
    index = st.slider("Which JD to select ? : ", 0,
                    len(Jobs['Name'])-1, 1)
    option_yn = st.selectbox("Show the Job Description ?", options=['YES', 'NO'])
    if option_yn == 'YES':
        st.markdown("---")
        st.markdown("### Job Description :")
        fig = go.Figure(data=[go.Table(
            header=dict(values=["Job Description"],
                        fill_color='#f0a500',
                        align='center', font=dict(color='white', size=16)),
            cells=dict(values=[Jobs['Context'][index]],
                    fill_color='#f4f4f4',
                    align='left'))])

        fig.update_layout(width=800, height=500)
        st.write(fig)
        st.markdown("---")
    return index

async def show_information_retrieval(Jobs, index):
    info_retrieval = extraction(Jobs, index)
    option_yn = st.selectbox("Information Retrieval ?", options=['YES', 'NO'])
    if option_yn == 'YES':
        st.markdown("---")
        st.markdown("### Information Retrieval :")
        fig = go.Figure(data=[go.Table(columnwidth = [1, 1, 2 , 3], header=dict(values=["Index", "Minimum degree level", "Acceptable majors", "Skills"], line_color='darkslategray',
                                                    fill_color='#f0a500'),
                                        cells=dict(values=[index, info_retrieval["Minimum degree level"], info_retrieval["Acceptable majors"], info_retrieval["Skills"]], line_color='darkslategray',
                                                    fill_color='#f4f4f4'))
                                ])

        fig.update_layout(width=800, height=500)
        st.write(fig)
        st.markdown("---")
    return info_retrieval

async def show_matching_rule(indexs, info_retrieval, resumes):
    results_matching = matching(info_retrieval, resumes)
    option_yn = st.selectbox("Matching Ruler by model All-mpnet-base-v2?", options=['YES', 'NO'])
    if option_yn == 'YES':
        indexs = [a for a in range(len(results_matching[0]["_id"]))]
        st.markdown("---")
        st.markdown("### Matching Ruler by model All-mpnet-base-v2 :")
        fig = go.Figure(data=[go.Table(columnwidth = [1, 2, 1 , 1, 2, 2], header=dict(values=["Index", "id", "Matching Scores", "Degrees", "Majors", "Skills"], line_color='darkslategray',
                                                    fill_color='#f0a500'),
                                        cells=dict(values=[indexs, results_matching[0]["_id"], results_matching[0]["matching score job 0"], results_matching[0]["degrees"], results_matching[0]["majors"], results_matching[0]["skills"]], line_color='darkslategray',
                                                    fill_color='#f4f4f4'))
                                ])
        fig.update_layout(width=800, height=500)
        st.write(fig)
        st.markdown("---")

    option_yn = st.selectbox("Matching Ruler by model SBERT Paraphrase-MiniLM-L6-v2?", options=['YES', 'NO'])
    if option_yn == 'YES':
        indexs = [a for a in range(len(results_matching[1]["_id"]))]
        st.markdown("---")
        st.markdown("### Matching Ruler by model SBERT Paraphrase-MiniLM-L6-v2 :")
        fig = go.Figure(data=[go.Table(columnwidth = [1, 2, 1 , 1, 2, 2], header=dict(values=["Index", "id", "Matching Scores", "Degrees", "Majors", "Skills"], line_color='darkslategray',
                                                    fill_color='#f0a500'),
                                        cells=dict(values=[indexs, results_matching[1]["_id"], results_matching[1]["matching score job 0"], results_matching[1]["degrees"], results_matching[1]["majors"], results_matching[1]["skills"]], line_color='darkslategray',
                                                    fill_color='#f4f4f4'))
                                ])
        fig.update_layout(width=800, height=500)
        st.write(fig)
        st.markdown("---")

    option_yn = st.selectbox("Matching Ruler by model SBERT Paraphrase-MiniLM-L12-v1?", options=['YES', 'NO'])
    if option_yn == 'YES':
        indexs = [a for a in range(len(results_matching[2]["_id"]))]
        st.markdown("---")
        st.markdown("### Matching Ruler by model SBERT Paraphrase-MiniLM-L12-v1:")
        fig = go.Figure(data=[go.Table(columnwidth = [1, 2, 1 , 1, 2, 2], header=dict(values=["Index", "id", "Matching Scores", "Degrees", "Majors", "Skills"], line_color='darkslategray',
                                                    fill_color='#f0a500'),
                                        cells=dict(values=[indexs, results_matching[2]["_id"], results_matching[2]["matching score job 0"], results_matching[2]["degrees"], results_matching[2]["majors"], results_matching[2]["skills"]], line_color='darkslategray',
                                                    fill_color='#f4f4f4'))
                                ])
        fig.update_layout(width=800, height=500)
        st.write(fig)
        st.markdown("---")


async def main():
    await asyncio.gather(load_title_dasboard())
    Resumes, Jobs, resumes = await asyncio.gather(load_input_data_Resumes(), load_input_data_Jobs(), load_input_data_resumes())
    _ , index  = await asyncio.gather(show_description_name(Jobs), show_description(Jobs))
    info_retrieval = await asyncio.gather(show_information_retrieval(Jobs, index))
    await asyncio.gather(show_matching_rule(index, info_retrieval[0], resumes))
asyncio.run(main())
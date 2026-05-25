import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the name of the new subject:")
    sub_id = st.text_input("Subject Code", placeholder="e.g. CS101")
    sub_name = st.text_input("Subject Name", placeholder="e.g. Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="e.g. A")

    if st.button("Create Subject", type='primary', width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast(f"Subject '{sub_name}' created successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred while creating the subject: {str(e)}")
        else:
            st.warning("Please fill in all fields to create a subject.")
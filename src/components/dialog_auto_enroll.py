import streamlit as st
from src.database.config import supabase
from src.database.db import enroll_student_to_subject
import time


@st.dialog("Quick Enroll")
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data['student_id']

    res = supabase.table('subjects').select('subject_id, name').eq('subject_code', subject_code).execute()
    if not res.data:
        st.error("Invalid subject code. Please check the code and try again.")
        if st.button("Close", type='secondary', width='stretch'):
            st.query_params.clear()
            st.rerun()
        return
    subject = res.data[0]

    check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
    if check.data:
        st.info(f"You are already enrolled in **{subject['name']}**.")
        if st.button("Got it", type='secondary', width='stretch'):
            st.query_params.clear()
            st.rerun()
        return
    st.markdown(f'Would you like to quickly enroll in [**{subject["name"]}**]?')

    col1, col2 = st.columns(2)

    with col1:
        if st.button('No'):
            st.query_params.clear()
            st.rerun()
        
    with col2:
        if st.button('Yes', type='primary', width='stretch'):
            enroll_student_to_subject(student_id, subject['subject_id'])
            st.success(f"Successfully enrolled in **{subject['name']}**!")
            time.sleep(1)
            st.query_params.clear()
            st.rerun()
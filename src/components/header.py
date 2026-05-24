import streamlit as st

def header_home():

    logo_url = "https://img.magnific.com/premium-vector/magnifying-glass-logo-people-finder-infinity-searching-vector_718429-1342.jpg?semt=ais_hybrid&w=740&q=80"
    st.markdown(
        f"""
        <div style="display: flex;flex-direction: column; align-items: center;justify-content: center; gap: 1rem;">
            <img src="{logo_url}" width="100" style="border-radius: 50%; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <h1 style="margin: 0; color: #007bff; text-align: center;">SnapVoice</h1>
        </div>
        """, unsafe_allow_html=True
    )
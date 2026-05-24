import streamlit as st

def style_background_home():

    st.markdown(
        """
            <style>
                .stApp {
                    background: #a2d2ff !important;
                }
                .stApp div[data-testid="stColumn"]{
                color: #333 !important;
                display: flex !important;
                flex-direction: row !important;
                align-items: center !important;
                justify-content: center !important;
                background-color: #fefefe !important;
                padding: 2rem !important;
                border-radius: 1rem !important;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
                }
            </style>
        """, unsafe_allow_html=True
    )
def style_background_dashboard():

    st.markdown(
        """
            <style>
                .stApp {
                    background-color: #d2b7e5 !important;
                }
            </style>
        """, unsafe_allow_html=True
    )
def style_base_layout():

    st.markdown(
        """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Kaushan+Script&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
                #MainMenu, footer, header{
                    visibility: hidden;
                }
                .block-container{
                    padding-top: 1.5rem !important;
                    padding-bottom: 2rem;
                    padding-left: 2rem;
                    padding-right: 2rem;
                }
                h1, h2{
                    font-family: 'Kaushan Script', cursive !important;
                    font-size: 3.5rem !important;
                    line-height: 1 !important;
                    margin-bottom: 0.6rem !important;
                }
                h3, h4, h5, h6, p{
                    font-family: 'Outfit', sans-serif !important;
                }
                button {
                    background: #007ea7 !important;
                    color: white !important;
                    border: none !important;
                    padding: 0.5rem 1.5rem !important;
                    border-radius: 0.5rem !important;
                    transition: transform 0.2s ease-in-out !important;
                    }
                button[kind='secondary'] {
                    background: #007ea7 !important;
                    color: white !important;
                    border: none !important;
                    padding: 0.5rem 1.5rem !important;
                    border-radius: 0.5rem !important;
                    transition: transform 0.2s ease-in-out !important;
                    }
                button[kind='tertiary'] {
                    background: #7251b5 !important;
                    color: white !important;
                    border: none !important;
                    padding: 0.5rem 1.5rem !important;
                    border-radius: 0.5rem !important;
                    transition: transform 0.2s ease-in-out !important;
                    }
                    button:hover {
                    transform: scale(1.05) !important;
                    }
            </style>
        """, unsafe_allow_html=True
    )


import streamlit as st
from src.database.db import check_teacher_exists, create_teacher, teacher_login
from src.components.footer import footer_dashboard
from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard

def teacher_screen():

    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state and st.session_state.teacher_data:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()

    
def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"Welcome, {teacher_data['name']}!")


def login_teacher(username, password):
    if not username or not password:
        return False, "Please enter both username and password."
    
    teacher = teacher_login(username, password)
    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True

def teacher_screen_login():
    c1, c2 = st.columns(2,vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button('Go to Dashboard', type='secondary', key='loginbackbutton'):
            st.session_state['login_type']= None
            st.rerun()

    st.header("Login")
    st.space()
    teacher_username = st.text_input("Enter Username")
    teacher_password = st.text_input("Enter Password", type="password")
    st.divider()
    
    btnc1,btnc2 = st.columns(2)
    with btnc1:
        if st.button('Login', icon=':material/login:', shortcut='Enter', width='stretch'):
            if login_teacher(teacher_username, teacher_password):
                st.toast("Welcome back!")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username or password. Please try again.")

    with btnc2:
        if st.button('Register Instead', type='primary', icon=':material/app_registration:', width='stretch'):
            st.session_state.teacher_login_type = 'register'   

    footer_dashboard()         
            

def register_teacher( teacher_name, teacher_username, teacher_password, teacher_confirm_password):
    if not teacher_name or not teacher_username or not teacher_password or not teacher_confirm_password:
        return False, "Please fill in all fields."
    
    if teacher_password != teacher_confirm_password:
        return False, "Passwords do not match."
    
    if check_teacher_exists(teacher_username):
        return False, "Username already exists. Please choose a different one."
    try:  
        create_teacher(teacher_username, teacher_password, teacher_name)
        return True, "Registration successful! You can now log in."
    except Exception as e:
        return False, f"An error occurred during registration: {str(e)}"


def teacher_screen_register():
    c1, c2 = st.columns(2,vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button('Go to Dashboard', type='secondary', key='loginbackbutton'):
            st.session_state['login_type']= None
            st.rerun()

    st.header("Register your teacher account")
    st.space()
    teacher_name = st.text_input("Enter Your Name")
    teacher_username = st.text_input("Enter Username")
    teacher_password = st.text_input("Enter Password", type="password")
    teacher_confirm_password = st.text_input("Confirm Password", type="password")
    st.divider()
    
    btnc1,btnc2 = st.columns(2)
    with btnc1:
        if st.button('Register', icon=':material/login:', shortcut='Enter', width='stretch'):
            success, message = register_teacher(teacher_name, teacher_username, teacher_password, teacher_confirm_password)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)

    with btnc2:
        if st.button('Go to Login', type='primary', icon=':material/app_registration:', width='stretch'):
            st.session_state.teacher_login_type = 'login'
            

    footer_dashboard()  
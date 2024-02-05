import streamlit as st
font_family = 'Calibri'
font_subheader_size = 20

box_color = '#003366'
border_top_color = '#FFFF66'
border_normal_color = '#3399FF'
border_size = '7px'

css_box_normal = f"""
    <style>
        .normal-box {{
            display: flex;
            justify-content: space-between; /* Aligns items on both ends of the flex container */
            background-color: {box_color};
            height: 100px;
            padding: 20px;
            border-radius: 10px;
            color: white;
            font-family: {font_family};
            font-size: 20px;
            text-align: left;
            border: {border_size} solid {border_normal_color};
            align-items: center; /* Aligns items vertically at the center */
        }}

        .normal-box .left-content {{
            text-align: left;
        }}

        .normal-box .right-content {{
            text-align: right;
            display: flex;
            flex-direction: column;
        }}

        .normal-box .acc {{
            color: #00FF00;
        }}

        .normal-box .notAcc {{
            color: #FF0000;
        }}
    </style>
"""

css_box_top = f"""
    <style>
        .top-box {{
            display: flex;
            justify-content: space-between;
            background-color: {box_color};
            height: 100px;
            padding: 20px;
            border-radius: 10px;
            color: white;
            font-family: {font_family};
            font-size: 20px;
            text-align: left;
            border: {border_size} solid {border_top_color};
            align-items: center;
        }}

        .top-box .left-content {{
            text-align: left;
        }}

        .top-box .right-content {{
            text-align: right;
            display: flex;
            flex-direction: column;
        }}

        .top-box .acc {{
            color: #00FF00;
        }}

        .top-box .notAcc {{
            color: #FF0000;
        }}
    </style>
"""

def back_ground_color():
    color = '#E9F5FF'
    page_bg_color = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-color: {color};
        }}
        </style>
        """
    st.markdown(page_bg_color, unsafe_allow_html=True)

def local_css(file_name):#func to read css file -> create flake
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

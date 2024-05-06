# streamlit run SB06.py

import streamlit as st
from streamlit_option_menu import option_menu

# https://icons.getbootstrap.com/
# https://discuss.streamlit.io/t/streamlit-option-menu-is-a-simple-streamlit-component-that-allows-users-to-select-a-single-item-from-a-list-of-options-in-a-menu/20514

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings', 'About'],
        icons=['house', 'gear', 'backpack'])
        # icons=['house', 'gear', 'backpack'], menu_icon="cast", default_index=1)

# supported colors: blue, green, orange, red, violet, gray/grey, rainbow
clr = 'rainbow'
if selected == "Home": clr = 'red'
if selected == "Settings": clr = 'green'
if selected == "About": clr = 'blue'
st.title(f"Welcome to the :{clr}[{selected}] page")

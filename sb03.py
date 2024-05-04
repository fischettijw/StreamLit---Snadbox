import streamlit as st

st.markdown('[Add widgets to sidebar](https://docs.streamlit.io/develop/api-reference/layout/st.sidebar)')

# Add a selectbox to the sidebar:
add_selectbox1 = st.selectbox(
    'How would you like to be contacted? (1)',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slide1 = st.slider(
    'Select a range of values (1)',
    0.0, 100.0, (25.0, 75.0)
)

# Add a selectbox to the sidebar:
add_selectbox2 = st.sidebar.selectbox(
    'How would you like to be contacted? (2)',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider2 = st.sidebar.slider(
    'Select a range of values (2)',
    0.0, 100.0, (25.0, 75.0)
)


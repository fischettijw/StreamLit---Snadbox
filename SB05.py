import streamlit as st

# Inject custom CSS to set the width of the sidebar
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 300px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Example sidebar content
st.sidebar.header("This is the sidebar")
st.sidebar.text("This is some text in the sidebar")

# Example main content
st.header("This is the Main Content Area")
st.text("This is some text in the main content area")
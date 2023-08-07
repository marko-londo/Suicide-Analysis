import streamlit as st
from Pages import page1, page2

st.set_page_config(page_title="Suicide Data Dashboard", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="auto", menu_items=None)

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
   
def main():
    

    # Add a sidebar
    st.sidebar.title("Navigation")
    page_options = ["Home", "U.S. Suicide Data by Year and Age Group", "Page 2"]
    selected_page = st.sidebar.radio("Select Page", page_options)

    # Show the selected page
    if selected_page == "Home":
        page1.show()
    elif selected_page == "U.S. Suicide Data by Year and Age Group":
        page2.show()
    elif selected_page == "Page 3":
        page3.show()

if __name__ == "__main__":
    main()


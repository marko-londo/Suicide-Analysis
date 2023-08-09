import streamlit as st
from Pages import page1, page2, page3, page4, page5, page6, page7, page8, page9

st.set_page_config(
    page_title="Suicide Data Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)


no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


def main():
    # Add a sidebar
    st.sidebar.title("Navigation")
    page_options = [
        "Home",
        "Exploring Suicides Trends Through Linear Regression",
        "Suicide Data by Year and Age Group",
        "Suicide Rates VS. Unemployment",
        "U.S. Suicides VS. Other Countries",
        "Divorce Rates VS. Suicide Rates",
        "Male Vs. Female Suicides",
        "Untreated Mental Illness in the United States",
        "988 Suicide & Crisis Lifeline Metrics",
    ]
    selected_page = st.sidebar.radio("Select Page", page_options)

    # Show the selected page
    if selected_page == "Home":
        page1.show()
    elif selected_page == "Suicide Data by Year and Age Group":
        page2.show()
    elif selected_page == "Suicide Rates VS. Unemployment":
        page3.show()
    elif selected_page == "Divorce Rates VS. Suicide Rates":
        page4.show()
    elif selected_page == "U.S. Suicides VS. Other Countries":
        page5.show()
    elif selected_page == "Exploring Suicides Trends Through Linear Regression":
        page6.show()
    elif selected_page == "Untreated Mental Illness in the United States":
        page7.show()
    elif selected_page == "Male Vs. Female Suicides":
        page8.show()
    elif selected_page == "988 Suicide & Crisis Lifeline Metrics":
        page9.show()


if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import holoviews as hv
import hvplot.pandas

us_suicides_total = pd.read_csv(r"../Resources/Clean/us_suicides_1985-2021.csv")


def show():
    col1, col2, col3 = st.columns([0.3, 1, 0.1])

    with col1:
        st.write(" ")

    with col2:
        st.image(
            "https://github.com/marko-londo/Suicide-Analysis/blob/main/Resources/Images/candles.png?raw=true",
            use_column_width="auto",
        )

    with col3:
        st.write(" ")
    st.markdown(
        "<h1 style='text-align: center;'>Suicide Data Dashboard<br><br></h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """

    ---

    """
    )

    us_suicides_total = pd.read_csv(r"../Resources/Clean/us_suicides_1985-2021.csv")

    hv_plot = us_suicides_total.hvplot(
        x="Year", y="Number of Suicides", rot=45, title="Total Suicides, U.S."
    ).opts(height=420, width=620, color="crimson", bgcolor="#121212")
    col4, col5 = st.columns([0.60, 0.45])
    with col4:
        st.write(hv.render(hv_plot, backend="bokeh"))

    with col5:
        st.markdown(
            """
Welcome to the interactive Suicide Data Dashboard—a powerful resource tailored
to illuminate the pressing issue of suicide. 
Through intuitive visualizations, this tool facilitates a deep exploration of
vital aspects in suicide research, such as:
- Suicide trends with linear regression
analysis. 
- Insights from U.S. suicide data, dissected by year and age
group. 
- Correlation between U.S. suicide rates and unemployment,
shedding light on potential societal links. 
- Gaining a global perspective by comparing U.S. suicide rates to those of other
countries. 
- Interplay between U.S. divorce rates and suicide
rates, revealing intricate connections within this critical conversation. 

Harness the knowledge provided here to engage in informed discussions, drive
awareness, and inspire action for mental health support and prevention.
To get started, use the sidebar to navigate between pages.
"""
        )

import streamlit as st
import pandas as pd
import holoviews as hv
import hvplot.pandas

us_suicides = pd.read_csv(r"../Resources/Clean/us_suicides_1985-2021.csv")
russia_suicides = pd.read_csv(r"../Resources/Clean/russia_suicides_1985-2016.csv")
paraguay_suicides = pd.read_csv(r"../Resources\Clean\paraguay_suicides_1985-2016.csv")
japan_suicides = pd.read_csv(r"../Resources\Clean\japan_suicides_1985-2016.csv")


def show():
    st.markdown(
        "<h1 style='text-align: center;'>U.S. Suicides VS. Other Countries<br><br></h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """ 
                Here we compare the number of suicides in the United States to
                Japan, Russia and Paraguay"""
    )

    st.markdown(
        """

    ---

    """
    )

    # Filter data for years up to 2014
    us_suicides_filtered = us_suicides[us_suicides["Year"] <= 2014]
    japan_suicides_filtered = japan_suicides[japan_suicides["Year"] <= 2014]
    russia_suicides_filtered = russia_suicides[russia_suicides["Year"] <= 2014]
    paraguay_suicides_filtered = paraguay_suicides[paraguay_suicides["Year"] <= 2014]

    fig = us_suicides_filtered.hvplot(
        x="Year", y="Number of Suicides", rot=45, title="U.S. Suicides"
    ).opts(height=420, width=550, color="darkslateblue")
    japan_plot = japan_suicides_filtered.hvplot(
        x="Year", y="Number of Suicides", rot=45, title="Japan Suicides"
    ).opts(height=420, width=550, color="mediumslateblue")
    col1, col2 = st.columns(2, gap="small")

    with col1:
        st.write(hv.render(fig, backend="bokeh"))
    with col2:
        st.write(hv.render(japan_plot, backend="bokeh"))

    russia_plot = russia_suicides_filtered.hvplot(
        x="Year", y="Number of Suicides", rot=45, title="Russia Suicides"
    ).opts(height=420, width=550, color="mediumpurple")
    paraguay_plot = paraguay_suicides_filtered.hvplot(
        x="Year", y="Number of Suicides", rot=45, title="Paraguay Suicides"
    ).opts(height=420, width=550, color="rebeccapurple")
    col3, col4 = st.columns(2)
    with col3:
        st.write(hv.render(russia_plot, backend="bokeh"))
    with col4:
        st.write(hv.render(paraguay_plot, backend="bokeh"))

    st.markdown("Some interesting insights from the data:")

    st.markdown(
        """
                - Russia's total suicides peaked in 1994 (economic fallout following the dissolution
          of the Soviet Union).
          
        - Japan's total suicides increased drastically from 1997 to 1998,
            following the Asian Financial Crisis.
        - Paraguay, the only developing country of the 4, has the lowest
          ammount of total suicides, however the number of suicides
          increased by 500% from 1985 to 2014
        """
    )

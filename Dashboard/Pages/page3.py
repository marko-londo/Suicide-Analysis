import streamlit as st
import pandas as pd
import holoviews as hv
from holoviews import opts
from bokeh.sampledata.unemployment1948 import data as bokeh_unemployment_df
import hvplot.pandas

us_suicide_rates = pd.read_csv(r"../Resources/Clean/us_suicide_rates_1985-2016.csv")

hv.extension("bokeh")


def show():
    st.markdown("<h1 style='text-align: center;'>U.S. Suicide Rates VS. Unemployment<br><br></h1>", unsafe_allow_html=True)
    st.markdown(""" On this page, we will compare the relationship between
                economic conditions and suicide rates in the United States. The
                visualizations below aim to demonstrate how economic fluctuations may influence psychological well-being.""")

    st.markdown("""

    ---

    """)
    col1, col2 = st.columns([0.625, 0.375])
    col3, col4 = st.columns([0.625, 0.375])
    # Transform the Bokeh sample data
    with col1:
        unemployment_data = bokeh_unemployment_df.copy()
        unemployment_data = unemployment_data.set_index("Year").drop("Annual", axis=1)
        unemployment_data = unemployment_data[unemployment_data.index >= 1980]

        # Reset the index to create a multi-index DataFrame
        unemployment_data = unemployment_data.reset_index().melt(
            id_vars="Year", var_name="Month", value_name="Unemployment"
        )

        # Create heatmap with HoloViews
        heatmap = hv.HeatMap(unemployment_data, ["Year", "Month"], "Unemployment").opts(
            opts.HeatMap(
                tools=["hover"],
                width=650,
                height=350,
                xrotation=45,
                colorbar=True,
                cmap="Viridis_r",
                title="Unemployment Rates, 1980-2016",
            )
        )

        # Display the Bokeh plot using st.bokeh_chart
        st.bokeh_chart(hv.render(heatmap, backend="bokeh"))

    with col2:
        st.write(
            "<span style='font-size: 14px;'>"
            """In the visual representation of unemployment rates, we
                 observe two significant peaks in economic history.
                 The first peak occurred during the years 1982-1983, a time
                 marked by economic turmoil and recession.
                 The unemployment rate surged during this period, reflecting
                 the challenges faced by the job market.
                 The second notable peak emerged after the global financial
                 crisis of 2007-2008. This period saw widespread job
                 losses and economic uncertainty, resulting in a spike in
                 unemployment."""
            "</span>",
            unsafe_allow_html=True,
        )

    with col3:
        hv_plot = us_suicide_rates.hvplot(x="Year", y="Suicides per 100k").opts(
            width=650, height=350, title="Suicide Rates, 1985-2015"
        )
        st.write(hv.render(hv_plot, backend="bokeh"))

    with col4:
        st.write(
            "<span style='font-size: 14px;'>"
            """When observing the U.S. suicide rates over time, a striking correlation
                 emerges between suicides and economic instability.
                 The years 1986-1987 stand as a poignant example, where a surge
                 in suicide rates
                 aligns with a period marked by economic turmoil. This link
                 between financial
                 instability and heightened psychological distress is
                 unmistakable, highlighting the far-reaching consequences
                 of economic challenges on individual well-being. Moreover,
                 the subsequent downward trajectory in suicide rates from 1987
                 to 2000
                 coincides with a period of relative economic stability,
                 illustrating the
                 potential positive impact of a conducive economic
                 environment on mental health. Nevertheless, the upturn in
                 suicide rates
                 around 2006 serves as a poignant reminder that the intricate
                 relationship
                 between economic factors and mental health remains a critical
                 societal concern,
                 warranting continued attention and proactive measures."""
            "</span>",
            unsafe_allow_html=True,
        )

import streamlit as st
import pandas as pd
import holoviews as hv
from bokeh.sampledata.us_marriages_divorces import data as bokeh_divorces_df
import hvplot.pandas

us_suicide_rates = pd.read_csv(r"../Resources/Clean/us_suicide_rates_1985-20161.csv")


def show():
    st.markdown(
        "<h1 style='text-align: center;'>U.S. Divorce Rates VS. Suicide Rates<br><br></h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """ 
                On this page, we investigate the potential relationship
                between two societal indicators; divorce and suicide. 
                By exploring how changes in divorce rates might coincide with
                shifts in suicide rates, 
                we aim to shed light on the complex interplay between social
                trends 
                and mental well-being."""
    )

    st.markdown(
        """

    ---

    """
    )

    divorces_df = bokeh_divorces_df.copy()
    filtered_divorces = divorces_df.loc[
        (divorces_df["Year"] >= 1985) & (divorces_df["Year"] <= 2006)
    ]

    suicide_head = us_suicide_rates.head(22)

    # Create the plots using hvplot
    divorces_plot = filtered_divorces.hvplot(
        x="Year", y="Divorces_per_1000", color="maroon"
    ).opts(width=570, title="Divorce Rates, 1985-2011")
    suicide_plot = suicide_head.hvplot(
        x="Year", y="Suicides per 100k", color="Violet"
    ).opts(width=570, title="Suicide Rates, 1985-2011")

    # Combine the plots using hv.Layout
    combined_layout = hv.Layout(divorces_plot + suicide_plot)

    # Display the combined layout using st.bokeh_chart()
    st.bokeh_chart(hv.render(combined_layout, backend="bokeh"))

    st.write(
        """As we delve into the data comparing divorce rates and suicide
             rates, a compelling correlation comes to light. 
             Over the years from 1985 to 2006, a period encompassing economic
             and societal shifts, 
             we observe a significant alignment. ***Notably, as divorce rates show
             a gradual decline, there is a 
             corresponding decrease in suicide rates***. While causation cannot be
             definitively inferred from this 
             observation alone, the parallel trends suggest a potential
             interdependence between marital 
             stability and mental well-being.

The charts provided on this page vividly depict these trends. ***The decline in divorce rates, 
illustrated in the maroon curve, mirrors the downward trajectory of the violet
curve representing 
suicide rates***. This striking similarity between the two curves prompts us to contemplate
the mechanisms that might link these societal indicators. Factors such as
social support 
networks, familial stability, and personal emotional resilience could
contribute 
to this correlation."""
    )

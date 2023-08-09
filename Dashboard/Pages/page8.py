import streamlit as st
import pandas as pd
import holoviews as hv
import hvplot.pandas



def show():
    st.markdown(
        "<h1 style='text-align: center;'>Male Vs. Female Suicides<br><br></h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """This section investigates the changing patterns of suicides among
        males and females, providing insights into the varying rates over
        different years. 
        By contrasting these trends, we gain a better understanding of gender-specific factors impacting suicide rates."""
    )
    st.markdown(
        """

    ---

    """
    )
    col1, col2 = st.columns([0.8, 0.2])
    us_suicides_master = pd.read_csv(
        r"../Resources/Clean/us_suicides_1985-2016(master).csv"
    )
    with col1:
        us_suicides_males = us_suicides_master[~(us_suicides_master["Sex"] == "female")]
        us_suicides_females = us_suicides_master[~(us_suicides_master["Sex"] == "male")]
        us_suicides_males = (
            us_suicides_males.groupby("Year")["Number of Suicides"].sum().reset_index()
        )
        us_suicides_females = (
            us_suicides_females.groupby("Year")["Number of Suicides"]
            .sum()
            .reset_index()
        )
        plots = (
            us_suicides_males.hvplot(
                x="Year", y="Number of Suicides", color="steelblue"
            ).opts(height=420, width=850, bgcolor="#121212")
            * us_suicides_females.hvplot(
                x="Year", y="Number of Suicides", color="mediumpurple"
            )
            * us_suicides_males.hvplot.scatter(
                x="Year", y="Number of Suicides", color="cornflowerblue"
            )
            * us_suicides_females.hvplot.scatter(
                x="Year", y="Number of Suicides", color="mediumslateblue"
            )
        )

        st.write(hv.render(plots, backend="bokeh"))

    with col2:
        st.markdown("##### Legend:")
        st.markdown("- <font color='steelblue'>Male</font>", unsafe_allow_html=True)
        st.markdown(
            "- <font color='mediumpurple'>Female</font>", unsafe_allow_html=True
        )

    st.markdown(
        """
                Key insights:
        - Males are much more likely to commit suicide than females.
        - Male suicides have increased by approximately 46.9% from 1985 to 2015.
        - Female suicides have increased by approximately 61.68% from 1985 to 2015.
        - The ratio of male to female suicides in 2015 was 3.33 to 1."""
    )

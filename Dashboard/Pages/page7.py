import streamlit as st
import pandas as pd
import holoviews as hv
import hvplot.pandas
import altair as alt


mental_illness_us = pd.read_csv(
    r"../Resources/Clean/untreated_mental_illness_total_2018-2019.csv"
)
mental_illness = pd.read_csv(
    r"../Resources/Clean/untreated_mental_illness_states_2018-2019.csv"
)


def show():
    st.markdown(
        "<h1 style='text-align: center;'>Untreated Mental Illness in the United States<br><br></h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """ 
                In this section we will explore the percentage of untreated
                adult mental illness cases in 2018-2019, exposing gaps in
                essential care for mental health. 
                - The initial plot provides an overview of the total cases nationwide.
                - The subsequent interactive plot allows customization through severity level and state filters."
                """
    )

    st.markdown(
        """

    ---

    """
    )
    col1, col2 = st.columns([0.85, 0.25])

    with col1:
        barplot = mental_illness_us.hvplot.bar().opts(
            colorbar=True,
            cmap="BuPu",
            ylim=(0, 100),
            ylabel="Percent",
            xlabel="Severity",
            height=420,
            width=850,
            title="Adults With Mental Illness Who Did Not Receive Treatment, 2018-2019",
        )
        st.write(hv.render(barplot, backend="bokeh"))
    with col2:
        st.markdown(
            """
                    - 67.9 percent of adults with mild mental illness
                      did not receive treatment.
                    - 53.5 percent of adults with moderate mental
                      illness did not receive treatment.
                    - 35 percent of adults (nearly 4 million) with severe mental illness did not receive treatment.
                    """
        )
    st.markdown(
        """

    ---

    """
    )

    col3, col4 = st.columns([0.15, 0.85])

    with col3:
        selected_severity = st.selectbox(
            "Select Severity Level:", ["Mild", "Moderate", "Serious"]
        )
        selected_states = st.multiselect(
            "Select States:", mental_illness["Location"].unique()
        )
    with col4:
        if selected_states:
            filtered_states_df = mental_illness[
                mental_illness["Location"].isin(selected_states)
            ]

            custom_y_format = alt.Y(
                selected_severity, title="Percentage", axis=alt.Axis(format="%")
            )

            color_scale = alt.Scale(
                domain=[0, 1],
                range=["#AEAFD7", "#372654"],
            )

            custom_y_format = alt.Y(
                selected_severity,
                title="Percentage",
                axis=alt.Axis(format="%"),
                scale=alt.Scale(domain=[0, 1]),
            )

            bar_chart = (
                alt.Chart(filtered_states_df)
                .mark_bar()
                .encode(
                    x=alt.X("Location", title="States"),
                    y=custom_y_format,
                    color=alt.Color(
                        selected_severity, title=selected_severity, scale=color_scale
                    ),
                    tooltip=["Location", selected_severity],
                )
                .properties(
                    title=f"{selected_severity} Mental Illness by State",
                    width=500,
                    height=650,
                )
            )
            st.altair_chart(bar_chart, use_container_width=True)

import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt


def show():
    df = pd.read_csv(r"../Resources/Clean/suicides_by_age_state_pop.csv")

    st.markdown(
        "<h1 style='text-align: center;'>U.S. Suicide Data by Year and Age Group<br><br></h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """By interacting with the choropleth map and box chart below, we can
                uncover critical insights such as:"""
    )

    st.markdown(
        """- Identifying states with high or low suicide rates in a
                  specific year.
- Comparing suicide trends across different age groups within a
                  state.
- Spotting any notable patterns or outliers in suicide rates.

    ---

    """
    )

    selected_year = st.slider(
        "Drag the slider to select a year:",
        min_value=df["Year"].min(),
        max_value=df["Year"].max(),
    )

    data = df.columns[2:]

    selected_age_group = st.selectbox("Select Data to Visualize:", data)

    filtered_df = df[(df["Year"] == selected_year) & (df[selected_age_group].notnull())]
    custom_color_scale = [
        "#6FC19A",
        "#66BDA3",
        "#5EB8AE",
        "#56AEB4",
        "#4E98AF",
        "#4680AB",
        "#3E68A6",
        "#364EA1",
        "#33389B",
        "#3D3095",
        "#4B2D8F",
        "#582A88",
        "#642782",
        "#6E247B",
        "#752273",
    ]

    col1, col2 = st.columns([0.65, 0.35])

    with col1:
        fig_choropleth = px.choropleth(
            filtered_df,
            locationmode="USA-states",
            locations="Location",
            scope="usa",
            color=selected_age_group,
            hover_name="Location",
            hover_data=[selected_age_group],
            title=f"United States ({selected_year}) - Data: {selected_age_group}",
            color_continuous_scale=custom_color_scale,
            width=700,
        )
        fig_choropleth.add_annotation(
            (
                dict(
                    font=dict(color="orchid", size=13),
                    x=0,
                    y=-0.12,
                    showarrow=False,
                    text="Note: States with insufficient data for Age Group/Year will display as all white",
                    textangle=0,
                    xanchor="left",
                    xref="paper",
                    yref="paper",
                )
            )
        )

        st.plotly_chart(fig_choropleth)

    with col2:
        selected_states = st.multiselect("Select states:", df["Location"].unique())
        if selected_states:
            filtered_states_df = filtered_df[
                filtered_df["Location"].isin(selected_states)
            ]
            bar_chart = (
                alt.Chart(filtered_states_df)
                .mark_bar()
                .encode(x="Location", y=selected_age_group)
                .properties(title=f"{selected_age_group}", width=400)
            )
            st.altair_chart(bar_chart)

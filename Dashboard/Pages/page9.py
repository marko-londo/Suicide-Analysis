import streamlit as st
import pandas as pd
import altair as alt

metrics_988 = pd.read_csv(
    r"../Resources/Clean/988_performance_metrics.csv"
)
metrics_988 = metrics_988.rename(columns={"Unnamed: 0": "Month"})
metrics_988 = metrics_988.iloc[::-1]

def show():
    st.markdown(
        "<h1 style='text-align: center;'>988 Suicide & Crisis Lifeline Metrics<br><br></h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """ 
                This section provides a straightforward overview of key metrics
                related to the 988 National Suicide Prevention Lifeline,
                offering insights into the lifeline's operational impact.
                """
    )
    st.markdown(
        """
 
    ---
 
    """)


    metrics_988["Month"] = pd.to_datetime(metrics_988["Month"])

    # Data transformation: melt the DataFrame to have a "Metrics" column
    melted_data = pd.melt(metrics_988, id_vars=["Month"], var_name="Metrics", value_name="Value")

    # Create a custom color scale for different metrics
    color_scale = alt.Scale(domain=["Routed Calls", "Routed Chats", "Routed Texts", "Total Routed"],
                            range=["#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd"])

    # Create the area chart
    area_chart = alt.Chart(melted_data).mark_area(opacity=0.3).encode(
        x=alt.X("Month:T", title="Month"),
        y=alt.Y("Value:Q", title="Value"),
        color=alt.Color("Metrics:N", scale=color_scale),
        tooltip=["Month:T", "Metrics:N", "Value:Q"]
    )

    # Display the Altair chart using st.altair_chart
    st.altair_chart(area_chart, use_container_width=True)

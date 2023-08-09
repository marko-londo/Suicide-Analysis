import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

metrics_988 = pd.read_csv(r"../Resources/Clean/988_performance_metrics.csv")
pct_988 = pd.read_csv(r"../Resources/Clean/988_pcts.csv")
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
 
    """
    )

    col1, col2 = st.columns([0.65, 0.35])
    with col1:
        color_map = {
            "Routed Calls": "cornflowerblue",
            "Routed Chats": "mediumpurple",
            "Routed Texts": "steelblue",
            "Total Routed": "darkslateblue",
        }
        fig1 = px.area(
            metrics_988,
            x="Month",
            y=["Routed Texts", "Routed Chats", "Routed Calls"],
            title="Total Routed Metrics",
            color_discrete_map=color_map,
        )
        fig1.update_yaxes(title_text="Value", scaleanchor="x", scaleratio=1)
        fig1.update_layout(title_text="988 Lifeline Metrics", width=725, height=420)
        st.plotly_chart(fig1)
    with col2:
        custom_colors = ["cornflowerblue", "mediumpurple", "steelblue", "darkslateblue"]
        fig2 = px.pie(
            pct_988,
            values="Percentage",
            names="Interaction Type",
            hole=0.3,
            color_discrete_sequence=custom_colors,
        )

        fig2.update_layout(title_text="Interaction Types", width=200, height=400)

        st.plotly_chart(fig2, use_container_width=True)
    col3, col4 = st.columns([0.65, 0.35])
    with col4:
        fig3 = px.bar(
            metrics_988,
            x=["Total Answered Percentage"],
            y="Month",
            title="Total Answered Percentages",
            orientation="h",
        )
        fig3.update_xaxes(title_text="Value")
        fig3.update_layout(width=450, height=400, showlegend=False)
        st.plotly_chart(fig3)
    with col3:
        fig1 = px.line(
            metrics_988,
            x="Month",
            y=["Total Routed"],
            title="Total Routed ",
            color_discrete_map=color_map,
        )
        fig1.update_yaxes(title_text="Total Routed", scaleanchor="x", scaleratio=1)
        fig1.update_layout(
            title_text="988 Total Routed Interactions",
            width=725,
            height=400,
            showlegend=False,
        )
        st.plotly_chart(fig1)

    st.markdown(
        """
 
    ---
 
    """
    )
    st.write(
        """The suicide/crisis hotline was changed from it's 10 digit phone number to 988 in July of 2022, with the goal of
             making it easier to connect with mental health professionals when in need. It can be
             called or texted at any time, 24 hours a day, 7 days a week."""
    )
    st.markdown(
        """
        Some positive news from the 988 Suicide & Crisis Lifeline:
        """
    )
    st.markdown(
        """
        - Total routed interactions increased 10.39% over it's first year.
        - By the end of the year, 93% of interactions were answered.
        - 4,008,282 interactions were routed.
        
        """
    )

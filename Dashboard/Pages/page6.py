import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.io import push_notebook, show, output_notebook

output_notebook()


def show():
    st.markdown(
        "<h1 style='text-align: center;'>Exploring Suicides Trends Through Linear Regression<br><br></h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """ This page displays a linear regression analysis of suicide trends
        over the years.
        It shows the statistical relationship between the yearly progression and changes in the number of suicides."""
    )

    st.markdown(
        """

    ---

    """
    )

    us_suicides_total = pd.read_csv(r"../Resources/Clean/us_suicides_1985-2021.csv")

    X = us_suicides_total[["Year"]]
    y = us_suicides_total["Number of Suicides"]

    model = LinearRegression()
    model.fit(X, y)

    slope = model.coef_[0]

    y_pred = model.predict(X)

    source_actual = ColumnDataSource(
        data=dict(
            x=us_suicides_total["Year"], y=us_suicides_total["Number of Suicides"]
        )
    )
    source_predicted = ColumnDataSource(
        data=dict(x=us_suicides_total["Year"], y=y_pred)
    )

    p = figure(
        title="Linear Regression Analysis",
        x_axis_label="Year",
        y_axis_label="Number of Suicides",
        plot_width=1000,
        plot_height=500,
    )
    p.scatter(x="x", y="y", source=source_actual, legend_label="Actual")
    p.line(
        x="x",
        y="y",
        source=source_predicted,
        line_color="red",
        legend_label="Predicted",
    )

    p.legend.title = "Trend"
    p.legend.label_text_font_size = "10pt"
    p.legend.location = "bottom_right"

    st.bokeh_chart(p)
    st.write("Slope (increase in suicides per year):", slope)

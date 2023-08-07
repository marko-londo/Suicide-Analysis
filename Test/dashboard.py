import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

# Load your data here
df = pd.read_csv(r"../Resources/Clean/suicides_by_age_state_pop.csv")

selected_year = st.slider('Drag the slider to select a year:', min_value=df['Year'].min(), max_value=df['Year'].max())

# Get the list of columns containing age groups (excluding 'Year' and 'Location' columns)
data = df.columns[2:-1]

selected_age_group = st.selectbox('Select Data to Visualize:', data)

# Correct the filtering condition based on 'Year' and the selected age group
filtered_df = df[(df['Year'] == selected_year) & (df[selected_age_group].notnull())]
custom_color_scale = [
    "#6FC19A", "#66BDA3", "#5EB8AE", "#56AEB4", "#4E98AF", "#4680AB", "#3E68A6",
    "#364EA1", "#33389B", "#3D3095", "#4B2D8F", "#582A88", "#642782", "#6E247B",
    "#752273"]




col1, col2 = st.columns(2)

with col1:
    # Choropleth Map
    fig_choropleth = px.choropleth(filtered_df, locationmode='USA-states', locations='Location', scope='usa',
                                color=selected_age_group, hover_name='Location', hover_data=[selected_age_group],
                                title=f'Suicide Data ({selected_year}) - Age Group: {selected_age_group}',
                                color_continuous_scale=custom_color_scale,
                                width=670)
    fig_choropleth.add_annotation((dict(font=dict(color='orchid',size=13),
                                            x=0,
                                            y=-0.12,
                                            showarrow=False,
                                            text="Note: States with insufficient data for Age Group/Year will display as all white",
                                            textangle=0,
                                            xanchor='left',
                                            xref="paper",
                                            yref="paper")))


    # Display the choropleth map
    st.plotly_chart(fig_choropleth)

with col2:        
    # Bar Chart
    selected_states = st.multiselect('Select states:', df['Location'].unique())
    if selected_states:
        filtered_states_df = filtered_df[filtered_df['Location'].isin(selected_states)]
        bar_chart = alt.Chart(filtered_states_df).mark_bar().encode(
            x='Location',
            y=selected_age_group
        ).properties(
            title=f'Total Suicides by State ({selected_year}) - Age Group: {selected_age_group}',
            width=500
        )
        st.altair_chart(bar_chart)
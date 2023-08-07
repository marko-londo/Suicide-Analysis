
import streamlit as st

def show():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image("https://github.com/marko-londo/Suicide-Analysis/blob/main/Resources/Images/candles.png?raw=true", use_column_width="auto")

    with col3:
        st.write(' ')
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("""Welcome to the interactive Suicide Data Dashboard – a
            powerful tool designed to shed light on a pressing and often
            overlooked societal issue. 
            The mission is to provide you with a comprehensive understanding
            of suicide data, 
            enabling you to explore key insights and trends from various angles.

In a world increasingly driven by data, it is crucial to confront complex
topics like suicide with informed analysis. 
This dashboard serves as a gateway to a wealth of information, offering
insights into suicide rates by state, 
age groups, and gender. The goal is to foster awareness, encourage informed discussions, and inspire action toward mental health
support and suicide prevention.

Through intuitive visualizations and user-friendly features, you will be able to:

- Explore by State and Age: Dive into suicide data across different states and
age ranges to identify patterns, outliers, and potential influencing factors.

- Global Comparisons: Gain a global perspective by comparing suicide rates with other countries, highlighting both shared challenges and unique differences.
- Gender Insights: Examine suicide data through a gender lens, recognizing the
distinct experiences and vulnerabilities that different genders face.

As you navigate through this dashboard, remember that each data point represents a life, a story, and a call to action. By engaging with this tool, you contribute to the ongoing dialogue on mental health, destigmatizing discussions around suicide, and fostering a more compassionate society.

Let us embark on this journey of understanding together. Click, explore, learn, and be part of the change we hope to inspire through this dashboard.""")

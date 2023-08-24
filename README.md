<p align="center">
  <img src="https://github.com/marko-londo/Suicide-Analysis/blob/main/Resources/Images/candles.png?raw=true" alt="Header Image">
</p>

# Suicide Data Analysis & Visualization

This repository presents an in-depth analysis of suicide rates and their correlation with various factors, culminating in an interactive Streamlit dashboard. The main objective of this project is to shine a light on this pressing public health issue and identify key determinants.

## Project Motivation

Suicide is a significant public health concern, claiming nearly 50,000 lives in the US in 2021. Through the exploration of this dataset, the primary aim was to understand the various factors that might lead someone to consider suicide, including geographic, societal, and economic dimensions. Initial findings indicate a notable correlation between suicide rates and economic distress.

The primary dataset, a global suicide database, was meticulously curated, emphasizing data pertinent to the United States. This data was complemented by information sourced from organizations such as the CDC, the 988 Suicide Lifeline, Kaggle, and more.

The subject of suicide has many facets, and while this project focused on certain aspects, many remain to be explored. Potential avenues for future investigation include veteran suicides and in-depth trends segmented by generations or locations.

## Repository Structure

- **Notebooks**
  - **data_cleaning.ipynb**: A Jupyter notebook detailing the data cleaning process. 
  - **suicides.ipynb**: Base visualizations offering a preliminary understanding of the data landscape.
- **Dashboard**: The main directory for the interactive Streamlit dashboard.
  - **Dashboard.py**: The primary script for the Streamlit app, which includes navigations to different pages, each highlighting various aspects of the data.
- **Resources**: Various data sources used in the project.

The Streamlit dashboard showcases a comprehensive exploration of suicide rates
and associated factors, using visualizations crafted with Bokeh, HoloViews, and
Plotly. 

## In-depth Analysis

### 1. Exploring Suicide Trends Through Linear Regression

This section provides a linear regression analysis of suicide trends over the years, shedding light on the statistical relationship between the progression of time and changes in the number of suicides. 

**Key Insight**: The data indicates an increase of approximately 533.46 suicides per year.

### 2. Suicide Data by Year and Age Group

By utilizing an interactive choropleth map and box chart, we derive several crucial insights:

- The ability to identify states with high or low suicide rates for a specific year.
- A comparison of suicide trends across different age groups within states.
- Identification of notable patterns or outliers in suicide rates.

**States of Concern**: Montana, Alaska, Washington State, and Wyoming consistently exhibit high suicide rates.

### 3. Economic Influence on Suicide Rates

This section delves into the relationship between the state of the economy, particularly unemployment rates, and suicide rates in the United States. The visualizations underline the potential impact of economic fluctuations on psychological well-being.

A close examination reveals two significant peaks in unemployment rates:

- **1982-1983**: Marked by economic turmoil and recession.
- **Post 2007-2008 Financial Crisis**: Widespread job losses and economic uncertainty.

When juxtaposed against U.S. suicide rates, a clear correlation emerges between
periods of economic instability and spikes in suicide rates. For instance, the
surge in suicides during 1986-1987 aligns with the tumultuous economic scenario
of that period. Conversely, the decrease in suicide rates from 1987 to 2000
coincides with an era of economic stability.


**Conclusion**: The complex interplay between economic factors and mental health underscores the necessity for continued exploration and intervention in this domain.

### 4. Comparing U.S. Suicides to Other Countries

In this segment, we explore the suicide trends in the United States in relation to three distinct countries: Japan, Russia, and Paraguay.

**Key Insights**:

- Russia experienced its peak in total suicides in 1994, potentially due to the economic consequences following the dissolution of the Soviet Union.
  
- Japan saw a significant rise in total suicides between 1997 and 1998, which aligns with the timeframe of the Asian Financial Crisis.
  
- Paraguay, while being the only developing country among the four, observed the lowest number of total suicides. Yet, it's concerning that the number of suicides in Paraguay surged by 500% from 1985 to 2014.

### 5. The Correlation Between Divorce Rates and Suicide

This section delves into the exploration of two societal indicators: divorce and suicide rates. By analyzing how changes in one might affect the other, we seek to understand the intricate dynamics between societal shifts and individual mental health.

**Key Observations**:

- There exists a noticeable correlation between the rates of divorce and suicide between 1985 to 2006. As divorce rates gradually decline during this period, there is a parallel decrease in suicide rates.

- The visualizations on this page distinctly highlight these trends. The maroon curve, representing divorce rates, closely tracks the violet curve which signifies suicide rates. 

- While causation isn't definitive, the alignment suggests potential interconnectedness between marital stability and mental health. Factors like familial stability, social support, and emotional resilience might play roles in this observed relationship.

### 6. Gender Differences in Suicide Rates

In this analysis, we delve into the gender-specific patterns of suicides over the years. Understanding these contrasts and trends offers insights into gender-related factors that might influence these rates.

**Key Findings**:

- Males exhibit a higher likelihood of committing suicide compared to females.
  
- From 1985 to 2015, male suicides rose by approximately 46.9%.
  
- Female suicides saw an increase of about 61.68% during the same period.
  
- The ratio of male-to-female suicides in 2015 stood at 3.33 to 1.

### 7. Untreated Mental Illness in the U.S.

This section unravels the concerning statistics of untreated mental illness cases among adults for the years 2018-2019. The goal is to highlight the critical care gaps in addressing mental health issues within the country.

**Findings**:

- **67.9%** of adults with *mild* mental illness remained untreated.
  
- **53.5%** of adults with *moderate* mental illness didn't receive the required treatment.
  
- A staggering **35%** of adults, translating to nearly 4 million individuals with *severe* mental illness, were left untreated.

The initial visualizations present a broad overview of the total cases nationwide. In contrast, the subsequent interactive plots allow users to delve deeper, offering customization through severity levels and state-based filtering.

### 8. Insights from the 988 National Suicide Prevention Lifeline

This section brings to light essential metrics and insights from the 988 National Suicide Prevention Lifeline. The insights aim to demonstrate the lifeline's impact in providing timely help and support to individuals in distress.

**Background**:

In July 2022, a landmark change was introduced to the suicide/crisis hotline. The hotline number was transitioned from its conventional 10-digit format to the shorter and more accessible '988'. This change was envisioned to simplify the process for individuals seeking urgent mental health assistance. The 988 helpline remains operational round the clock, 24/7, ready to attend both calls and texts.

**Key Metrics**:

- The total interactions routed through the 988 Lifeline saw an increase of **10.39%** during its first year of operation.
  
- By the close of the year, an impressive **93%** of all interactions received a response.
  
- The lifeline successfully routed a total of **4,008,282 interactions** over the year.






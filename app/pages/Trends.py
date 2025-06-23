import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# -- Title --
st.title("📈 Inefficiency Trends Dashboard")

# -- Load Data --
df_front = pd.read_csv('data/df_all_year.csv')

# -- Sidebar Country Selection --
countries = sorted(df_front['Country Code'].unique())
selected_country = st.selectbox("Select Country", countries)

# -- Filter and Transform Data --
df_country = df_front[df_front['Country Code'] == selected_country].copy()
df_country = df_country.sort_values("year")

df_country['exp_mortality'] = np.exp(-df_country['y'])  # assuming y = -log(mortality)
df_country['exp_expenditure'] = np.exp(df_country['x'])  # assuming x = log(expenditure)

# ========== 1. Under-5 Mortality Trend ==========
st.markdown("#### Under-5 Mortality Trend")
fig_mortality = go.Figure()

fig_mortality.add_trace(go.Scatter(
    x=df_country['year'],
    y=df_country['exp_mortality'],
    mode='lines+markers',
    name='Observed Mortality',
    line=dict(color='blue'),
    hovertemplate='Year: %{x}<br>Mortality: %{y:.2f}'
))

fig_mortality.update_layout(
    xaxis_title="Year",
    yaxis_title="U5 Mortality Rate",
    height=350,
    margin=dict(t=10, b=10)
)

st.plotly_chart(fig_mortality, use_container_width=True)

# ========== 2. Health Expenditure ==========
st.markdown("#### Health Expenditure per Capita")
fig_expend = go.Figure()

fig_expend.add_trace(go.Scatter(
    x=df_country['year'],
    y=df_country['exp_expenditure'],
    mode='lines+markers',
    name='Health Expenditure',
    line=dict(color='orange'),
    hovertemplate='Year: %{x}<br>Expenditure: %{y:.2f}'
))

fig_expend.update_layout(
    xaxis_title="Year",
    yaxis_title="Expenditure per Capita",
    height=350,
    margin=dict(t=10, b=10)
)

st.plotly_chart(fig_expend, use_container_width=True)

# ========== 3. Inefficiency Plot ==========
st.markdown("#### Inefficiency Over Time")
fig_ineff = go.Figure()

fig_ineff.add_trace(go.Scatter(
    x=df_country['year'],
    y=df_country['ineff'],
    mode='lines+markers',
    name='Inefficiency',
    line=dict(color='red'),
    hovertemplate='Year: %{x}<br>Inefficiency: %{y:.3f}'
))

fig_ineff.update_layout(
    xaxis_title="Year",
    yaxis_title=None,  # No y-axis label
    height=400,
    margin=dict(t=10, b=10),
    yaxis=dict(showticklabels=True, title=None)
)

st.plotly_chart(fig_ineff, use_container_width=True)

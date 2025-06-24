import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
# df = pd.read_csv('../df_display.csv')
# df_raw = pd.read_csv('../data/results_csv/frontier_data_final.csv')
# df_front = pd.read_csv('../data/df_all_year.csv')
df_front = pd.read_csv('app/data/df_all_year.csv')


# df_1 = df_raw[['ihme_pe','ihme_high','ihme_low','ihme_hcepc','Urban_sh','Country Code','year','sdi','Urban_sh','corruption', 'peace_stab', 'regulatory','mean_chw', 'mean_nurse', 'mean_pharm', 'mean_phys']]
# df_1['ihme_pe'] = np.log(df_1['ihme_pe'])
# df_1['ihme_high'] = np.log(df_1['ihme_high'])
# df_1['ihme_low'] = np.log(df_1['ihme_low'])
# df_1['ihme_hcepc'] = np.log(df_1['ihme_hcepc'])
# df_1['Country Code'] = df_1['Country Code']
# df_1['se'] = (df_1['ihme_high'] - df_1['ihme_low']) / (2 * 1.96)
# df = df_1[['ihme_pe','ihme_hcepc','se','Country Code','year','sdi','Urban_sh','corruption', 'peace_stab', 'regulatory','mean_chw', 'mean_nurse', 'mean_pharm', 'mean_phys']]
# df.columns = ['y','x','se','Country Code','year','sdi', 'pop_sh', 'Urban_sh','corruption', 'peace_stab', 'regulatory',
#        'intercept', 'mean_chw', 'mean_nurse', 'mean_pharm', 'mean_phys']


'''
Functions for Year SFMA modeling 
'''
# Two-column layout
# left_col, right_col = st.columns([1, 3])  # Left narrow, right wider

# with left_col:
#     st.markdown("### 📅 Year Selection")
#     selected_year = st.selectbox("Select a Year", sorted(df_front['year'].unique()))

# # Filter data for selected year
# df_year = df_front[df_front['year'] == selected_year]
# df_year['y'] = -df_year['y']
# df_year['pred'] = -df_year['pred']


# with right_col:
#     st.markdown(f"### 📊 Efficiency Frontier Plot for {selected_year}")

#     x = df_year['x']
#     y = df_year['y']
#     pred = df_year['pred']
#     labels = df_year['Country Code']
#     sdi = df_year['sdi_cat']

#     # Plot with seaborn
#     fig, ax = plt.subplots()
#     sns.scatterplot(
#         data=df_year,
#         x='x',
#         y='y',
#         hue='sdi_cat',
#         style='sdi_cat',
#         s=70,
#         edgecolor='black',
#         alpha=0.8,
#         palette='Set1',
#         ax=ax
#     )

#     # Annotations
#     for i, label in enumerate(labels):
#         ax.annotate(label, (x.iloc[i], y.iloc[i]), textcoords="offset points",
#                     xytext=(0, 5), ha='center', fontsize=6)

#     # Prediction line
#     ax.plot(x, pred, color="black", linestyle='-.', linewidth=2)

#     # Axes labels and title
#     ax.set_xlabel('Healthcare expenditure per capita')
#     ax.set_ylabel('Under five mortality rate')
#     ax.set_title(f"Efficiency Frontier Plot - {selected_year}")

#     # Adjust plot size
#     golden_ratio = 1.618
#     width = 8
#     height = width / golden_ratio
#     fig.set_size_inches(width, height)

#     st.pyplot(fig)

#     # df_front.sort_values(by = 'inefc')
#     ### Table for thop and bottom 3 efficient countries

#     st.markdown("### 🌟 Top 3 Most Efficient Countries")
#     top3 = df_year.sort_values(by='ineff').head(5)[['Country Code', 'x','y', 'ineff', 'sdi_cat' ]]
#     st.dataframe(top3.reset_index(drop=True), use_container_width=True)

#     st.markdown("### 🚨 Bottom 3 Least Efficient Countries")
#     bottom3 = df_year.sort_values(by='ineff', ascending=False).head(3)[['Country Code', 'x','y', 'ineff', 'sdi_cat']]
#     st.dataframe(bottom3.reset_index(drop=True), use_container_width=True)


#     st.markdown("### Prediction")


# Two-column layout
left_col, right_col = st.columns([1, 3])

with left_col:
    st.markdown("### 📅 Year Selection")
    selected_year = st.selectbox("Select a Year", sorted(df_front['year'].unique()))

# Filter data
df_year = df_front[df_front['year'] == selected_year].copy()


df_year['y'] = -df_year['y']
df_year['pred'] = -df_year['pred']
# Filter: use only rows where pred > 0 for valid frontier
df_year = df_year[df_year['pred'] > 0].copy()

# Compute efficiency %
df_year['efficiency (%)'] = (1 - df_year['ineff']) * 100

with right_col:
    st.markdown(f"### 📊 Efficiency Frontier Plot for {selected_year}")

    fig, ax = plt.subplots()
    sns.scatterplot(
        data=df_year,
        x='x',
        y='y',
        hue='sdi_cat',
        style='sdi_cat',
        s=70,
        edgecolor='black',
        alpha=0.8,
        palette='Set1',
        ax=ax
    )

    # Country code annotations
    for i, label in enumerate(df_year['Country Code']):
        ax.annotate(label, (df_year['x'].iloc[i], df_year['y'].iloc[i]),
                    textcoords="offset points", xytext=(0, 5), ha='center', fontsize=6)

    # Frontier line (raw log-scale)
    ax.plot(df_year['x'], df_year['pred'], color="black", linestyle='-.', linewidth=2)

    ax.set_xlabel('log(Healthcare expenditure per capita)')
    ax.set_ylabel('log(Under-five mortality rate)')
    ax.set_title(f"Efficiency Frontier Plot - {selected_year}")

    golden_ratio = 1.618
    width = 8
    height = width / golden_ratio
    fig.set_size_inches(width, height)

    st.pyplot(fig)

    # --- Prepare Clean Tables for Display ---

df_table = df_year.copy()
df_table['Health Exp (pc)'] = np.exp(df_table['x']).round(2)
df_table['U5 Mortality'] = np.exp(df_table['y']).round(2)
# df_table['Predicted U5MR'] = np.exp(df_table['pred']).round(2)
df_table['Efficiency (%)'] = ((1 - df_table['ineff']) * 100).round(1)

# Columns to display
display_cols = [
    'Country Code',
    'Health Exp (pc)',
    'U5 Mortality',
    # 'Predicted U5MR',
    # 'Efficiency (%)',
    'sdi_cat',
    # 'pred'
]

# Top 3 most efficient
st.markdown("### 🌟 Top 3 Most Efficient Countries")
top3 = df_table.sort_values(by='Efficiency (%)', ascending=False).head(3)[display_cols]
st.dataframe(top3.reset_index(drop=True), use_container_width=True)

# Bottom 3 least efficient
st.markdown("### 🚨 Bottom 3 Least Efficient Countries")
bottom3 = df_table.sort_values(by='Efficiency (%)', ascending=True).head(3)[display_cols]
st.dataframe(bottom3.reset_index(drop=True), use_container_width=True)

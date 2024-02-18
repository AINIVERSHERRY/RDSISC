import pandas as pd
import streamlit as st


st.header('售前项目')
df_sq = pd.read_excel('./data/xmhz.xlsx')
st.write(df_sq)

st.header('正式项目')
df_zs = pd.read_excel('./data/xmhz.xlsx', sheet_name='正式项目')
st.write(df_zs)

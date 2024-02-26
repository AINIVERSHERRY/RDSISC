import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="中国区域数据资源共享社区",
    page_icon="🌍",
)


st.header('售前项目')
df_sq = pd.read_excel('./data/xmhz.xlsx')
st.write(df_sq)

st.header('正式项目')
df_zs = pd.read_excel('./data/xmhz.xlsx', sheet_name='正式项目')
st.write(df_zs)


footer="""<style>.footer {
position: fixed;left: 0;bottom: 0;width: 100%;background-color: white;color: black;text-align: center;
}
</style>
<div class="footer">
<p>xin.jin02@hlifetech.com</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

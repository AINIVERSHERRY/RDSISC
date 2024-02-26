import streamlit as st


st.set_page_config(
    page_title="中国区域数据资源共享社区",
    page_icon="🌍",
)


st.write('支持通过 LLM 对话式查询')


footer="""<style>.footer {
position: fixed;left: 0;bottom: 0;width: 100%;background-color: white;color: black;text-align: center;
}
</style>
<div class="footer">
<p>xin.jin02@hlifetech.com</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

import streamlit as st


st.set_page_config(
    page_title="中国区域数据资源共享社区",
    page_icon="🌍",
)


# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors].''')


multi = """
:orange[Q: 需要提前多久提交探查需求？]

A: 从供应商收到需求到反馈 5-7 天，如果前序有其他探查正在进行，需要排队等待。


:orange[Q: 区域数据合同金额一般多少钱？]

A: 供应商根据项目复杂程度报价。

"""
st.markdown(multi)


footer="""<style>.footer {
position: fixed;left: 0;bottom: 0;width: 100%;background-color: white;color: black;text-align: center;
}
</style>
<div class="footer">
<p>xin.jin02@hlifetech.com</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

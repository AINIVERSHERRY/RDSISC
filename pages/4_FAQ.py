import streamlit as st


st.set_page_config(
    page_title="中国区域数据资源共享社区",
    page_icon="🌍",
)


# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors].''')


multi = """
Q: 需要提前多久提交探查需求？

A: 从供应商收到需求到反馈5-7天，如果前序有其他探查正在进行，需要排队等待。


Q: 区域数据合同金额一般多少钱？

A: 供应商根据项目复杂程度报价。已签订RWS合同的金额在8-15w之间，新项目估计报价不会比15w低太多；已签订MIC合同金额3.4w。

"""
st.markdown(multi)

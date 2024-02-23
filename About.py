import streamlit as st


st.set_page_config(
    page_title="中国区域医疗数据资源共享社区",
    page_icon="🌍",
    # layout="wide",
    # initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'xin.jin02@hlifetech.com',
    #     'Report a bug': "xin.jin02@hlifetech.com",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)


st.markdown("""
RDSISC（Regional data source information sharing community）是一个开源的区域医疗数据源社区，我们汇集行业内各个参与方的数据源信息，目的是提高项目匹配效率，快速高效的为 MIC 和 RWE 等项目找到最合适的区域数据源！进一步，可以推动国内健康数据要素流动，促进数据价值释放。

- Map 页面支持按省份查询该地区的基本信息、供应商名单、已有项目情况

- Projects 页面提供了区域数据源已有项目列表，可以根据疾病、用药等字段查询信息。后续我们会上传已有项目的探查规则及探查结果，大家可以根据需要选用

- Chat2Source 页面支持对话式查询供应商和项目信息

""")

footer="""<style>.footer {
position: fixed;left: 0;bottom: 0;width: 100%;background-color: white;color: black;text-align: center;
}
</style>
<div class="footer">
<p>xin.jin02@hlifetech.com</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

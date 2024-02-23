import streamlit as st


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

# st.caption('（十一）数据要素×医疗健康提升群众就医便捷度，探索推进电子病历数据共享，在医疗机构间推广检查检验结果数据标准统一和共享互认。便捷医疗理赔结算，支持医疗机构基于信用数据开展先诊疗后付费就医。推动医保便民服务。依法依规探索推进医保与商业健康保险数据融合应用，提升保险服务水平，促进基本医保与商业健康保险协同发展。有序释放健康医疗数据价值，完善个人健康数据档案，融合体检、就诊、疾控等数据，创新基于数据驱动的职业病监测、公共卫生事件预警等公共服务模式。加强医疗数据融合创新，支持公立医疗机构在合法合规前提下向金融、养老等经营主体共享数据，支撑商业保险产品、疗养休养等服务产品精准设计，拓展智慧医疗、智能健康管理等数据应用新模式新业态。提升中医药发展水平，加强中医药预防、治疗、康复等健康服务全流程的多源数据融合，支撑开展中医药疗效、药物相互作用、适应症、安全性等系统分析，推进中医药高质量发展。')
# st.write('国家数据局：https://www.thepaper.cn/newsDetail_forward_25902357')
# st.markdown('''
# :balloon:待讨论：            
#     1. 闭源 or 开源？
#     2. 数据源信息是核心，开源可以更好更快的扩大和占据核心信息
#     3. 开源怎么盈利？怎么拉动客户和供应商加入生态？
# ''')
# st.markdown('''
# :balloon:受益方：数据需求方、咨询服务类公司、数据供应商
# ''')

import json
import pandas as pd
import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Map
from streamlit_echarts import Map as st_Map
from streamlit_echarts import st_pyecharts


st.set_page_config(
    page_title="中国区域数据资源共享社区",
    page_icon="🌍",
)


df = pd.read_excel('./data/dyb.xlsx', skiprows=1)
df_tmp = df[['大区', '省']].groupby('省').count()
res = []
for area in df_tmp.index:
    if area != 'ALL':
        # numpy.int64 vs int
        # 将数据传入到 pyecharts 的时候，需要自行将数据格式转换成上述 Python 原生的数据格式
        res.append((area, int(df_tmp.loc[area, '大区'])))


# 覆盖地图
with open("./data/china.geo.json", "r") as f:
    map = st_Map("china", json.loads(f.read()),)
c = Map(init_opts=opts.InitOpts(bg_color="white"))
c.add("区域数据源概览", res, "china")
c.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        showLegendSymbol=False,
        )
c.set_global_opts(
    # title_opts=opts.TitleOpts(title="Map china"),
    visualmap_opts=opts.VisualMapOpts(max_=max([i for _, i in res])),
)
st_pyecharts(c, map=map, height=500)


# 筛选按钮
option = st.selectbox(
   label="",
   options=[f"{i[0]}" for i in res],
   index=None,
   placeholder="请选择关注的区域",
)


# 区域信息
tab1, tab2, tab3 = st.tabs(["区域基本信息", "供应商名单", "既往合作项目"])
if option:
    with tab1:
        # df_tmp = df[['三甲.2', '三级.2', '二级.2', '总.2', '区域人口数量\n（截止2021年）']][df['省'] == option].iloc[0, 0:]
        # st.write(f"{option}2021年常住人口{df_tmp['区域人口数量\n（截止2021年）']}万，该地区有{df_tmp['三甲.2']}家三甲医院")
        st.write(df[['三甲.2', '三级.2', '二级.2', '总.2', '区域人口数量\n（截止2021年）']][df['省'] == option].iloc[0, 0:])
    with tab2:
        df_tmp = df[df['省'] == option].sort_values(['供应商名称', '数据源名称']).reset_index(drop=True).fillna('')
        row1 = st.columns(2)
        row2 = st.columns(2)
        row3 = st.columns(2)
        for idx, col in enumerate(row1 + row2 + row3):
            if idx <= max(df_tmp.index):
                tile = col.container(border=True)
                tile.markdown("🔻%s-%s" % (df_tmp.loc[idx, '供应商名称'].replace(' ', '').replace('\n', ''), df_tmp.loc[idx, '数据源名称'].replace('（', '-').replace('）', '').replace(' ', '').replace('\n', '')))
                tile.markdown(f"覆盖地区：{df_tmp.loc[idx, '市'] if df_tmp.loc[idx, '市'] != 'ALL' else option}")
                tile.markdown("患者总量：%s万" % int(df_tmp.loc[idx, '总患者数量\n（万）']) if df_tmp.loc[idx, '总患者数量\n（万）'] != '' else '患者总量：未知')
                tile.markdown(f"时间范围：{df_tmp.loc[idx, '数据时间范围']}" if df_tmp.loc[idx, '数据时间范围'] != '' else '时间范围：未知')
                tile.markdown("数据获取方式：%s" % df_tmp.loc[idx, '数据获取方式\n（直连/上报/抄数...）'] if df_tmp.loc[idx, '数据获取方式\n（直连/上报/抄数...）'] != '' else '数据获取方式：未知')
                # 地区代表性
                if df_tmp.loc[idx, '总.1'] == '':
                    tile.markdown(f"医院总数：未知")
                else:
                    tile.markdown(f"医院总数：{int(df_tmp.loc[idx, '总.1'])}")
                # 三甲医院覆盖情况
                numerator = int(df_tmp.loc[idx, '三甲.1']) if df_tmp.loc[idx, '三甲.1'] != '' else 'null'
                denominator = int(df_tmp.loc[idx, '三甲.2']) if df_tmp.loc[idx, '三甲.2'] != '' else 'null'
                if numerator == 'null' or denominator == 'null':
                    tile.markdown("三甲覆盖比例：未知（%s/%s）" % (numerator, denominator))
                else:
                    tile.markdown("三甲覆盖比例：%s%s（%s/%s）" % (int(100*numerator/denominator), '%', numerator, denominator))
                # 三级医院覆盖情况
                numerator = int(df_tmp.loc[idx, '三级.1']) if df_tmp.loc[idx, '三级.1'] != '' else 'null'
                denominator = int(df_tmp.loc[idx, '三级.2']) if df_tmp.loc[idx, '三级.2'] != '' else 'null'
                if numerator == 'null' or denominator == 'null':
                    tile.markdown("三级覆盖比例：未知（%s/%s）" % (numerator, denominator))
                else:
                    tile.markdown("三级覆盖比例：%s%s（%s/%s）" % (int(100*numerator/denominator), '%', numerator, denominator))
                # 二级医院覆盖情况
                numerator = int(df_tmp.loc[idx, '二级.1']) if df_tmp.loc[idx, '二级.1'] != '' else 'null'
                denominator = int(df_tmp.loc[idx, '二级.2']) if df_tmp.loc[idx, '二级.2'] != '' else 'null'
                if numerator == 'null' or denominator == 'null':
                    tile.markdown("二级覆盖比例：未知（%s/%s）" % (numerator, denominator))
                else:
                    tile.markdown("二级覆盖比例：%s%s（%s/%s）" % (int(100*numerator/denominator), '%', numerator, denominator))
    with tab3:
        st.write('需要和项目数据库关联')


footer="""<style>.footer {
position: fixed;left: 0;bottom: 0;width: 100%;background-color: white;color: black;text-align: center;
}
</style>
<div class="footer">
<p>xin.jin02@hlifetech.com</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

import json
import pandas as pd
import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from streamlit_echarts import Map as st_Map
from streamlit_echarts import st_pyecharts


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
        label_opts=opts.LabelOpts(is_show=False)
        , showLegendSymbol=False
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
#    options=[i[0] for i in res],
   index=None,
   placeholder="请选择关注的区域",
)
# st.write('You selected:', option)


# 区域信息
tab1, tab2, tab3 = st.tabs(["区域基本信息", "供应商名单", "既往合作项目"])
if option:
    with tab1:
        # st.header("a cat")
        # st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        st.write(df[['三甲.2', '三级.2', '二级.2', '总.2', '区域人口数量\n（截止2021年）']][df['省'] == option].iloc[0, 0:])
    with tab2:
        # st.header("a dog")
        # st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
        # st.write(df[['区域数据源名称', '大区', '省', '市', '三甲', '三级', '二级', '总', '总患者数量\n（万）', '数据时间范围', '数据获取方式\n（直连/上报/抄数...）', '是否需要卫建委审批', '是否支持\n驻场', '是否已有合作']][df['省'] == option].sort_values('区域数据源名称').reset_index(drop=True))
        df_tmp = df[df['省'] == option].sort_values('区域数据源名称').reset_index(drop=True).fillna('')
        row1 = st.columns(3)
        row2 = st.columns(3)
        row3 = st.columns(3)
        for idx, col in enumerate(row1 + row2 + row3):
            if idx <= max(df_tmp.index):
                # label = f"{df_tmp.loc[idx, '区域数据源名称'].replace('\n', '-')}-{df_tmp.loc[idx, '市'] if df_tmp.loc[idx, '市'] != 'ALL' else option}"
                # tile = col.expander(label)
                tile = col.container(border=True)
                # tile.title('🎈')
                tile.markdown("🔻%s" % df_tmp.loc[idx, '区域数据源名称'].replace('\n', '-'))
                tile.markdown(f"覆盖地区：{df_tmp.loc[idx, '市'] if df_tmp.loc[idx, '市'] != 'ALL' else option}")
                tile.markdown("患者总量（万）：%s" % int(df_tmp.loc[idx, '总患者数量\n（万）']) if df_tmp.loc[idx, '总患者数量\n（万）'] != '' else '未知')
                tile.markdown(f"时间范围：{df_tmp.loc[idx, '数据时间范围']}")
                tile.markdown("数据获取方式：%s" % df_tmp.loc[idx, '数据获取方式\n（直连/上报/抄数...）'])
                # 地区代表性
                if df_tmp.loc[idx, '三甲.1'] == '' or df_tmp.loc[idx, '三甲.2'] == '':
                    tile.markdown(f"三甲覆盖比例：未知")
                else:
                    tile.markdown(f"三甲覆盖比例：{int(100 * df_tmp.loc[idx, '三级.1']/df_tmp.loc[idx, '三级.2'])}%")
                if df_tmp.loc[idx, '三级.1'] == '' or df_tmp.loc[idx, '三级.2'] == '':
                    tile.markdown(f"三级覆盖比例：未知")
                else:
                    tile.markdown(f"三级覆盖比例：{int(100 * df_tmp.loc[idx, '三级.1']/df_tmp.loc[idx, '三级.2'])}%")
                if df_tmp.loc[idx, '二级.1'] == '' or df_tmp.loc[idx, '二级.2'] == '':
                    tile.markdown(f"二级覆盖比例：未知")
                else:
                    tile.markdown(f"二级覆盖比例：{int(100 * df_tmp.loc[idx, '二级.1']/df_tmp.loc[idx, '二级.2'])}%")
        # st.write(set(df[df['省'] == option]['区域数据源名称']))
    with tab3:
        #    st.header("owl")
        # st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
        st.write('需要和项目数据库关联')

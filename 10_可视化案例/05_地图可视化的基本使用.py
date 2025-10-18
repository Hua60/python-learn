from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

# 修改为完整的省级行政区名称
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499)
]

map.add("测试地图", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 100, "label": "1-100", "color": "#CCFFFF"},
            {"min": 101, "max": 300, "label": "101-300", "color": "#FF6666"},
            {"min": 301, "max": 500, "label": "301-500", "color": "#990033"}
        ]
    )
)

map.render()

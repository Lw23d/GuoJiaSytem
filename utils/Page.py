from typing import List

import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line

data = [
    {
        "time": "2010年",
        "data": [
            {"name": "广东省", "value": [104320459, 10.53, "广东省"]},
            {"name": "江苏省", "value": [78660941, 9.48, "江苏省"]},
            {"name": "山东省", "value": [95792719, 8.96, "山东省"]},
            {"name": "浙江省", "value": [54426891, 6.34, "浙江省"]},
            {"name": "河南省", "value": [94029939, 5.28, "河南省"]},
            {"name": "河北省", "value": [71854210, 4.67, "河北省"]},
            {"name": "辽宁省", "value": [43746323, 4.22, "辽宁省"]},
            {"name": "四川省", "value": [80417528, 3.93, "四川省"]},
            {"name": "上海市", "value": [23019196, 3.93, "上海市"]},
            {"name": "湖南省", "value": [65700762, 3.67, "湖南省"]},
            {"name": "湖北省", "value": [57237727, 3.65, "湖北省"]},
            {"name": "福建省", "value": [36894217, 3.37, "福建省"]},
            {"name": "北京市", "value": [19612368, 3.23, "北京市"]},
            {"name": "安徽省", "value": [59500468, 2.83, "安徽省"]},
            {"name": "内蒙古", "value": [24706291, 2.67, "内蒙古"]},
            {"name": "黑龙江省", "value": [38313991, 2.37, "黑龙江省"]},
            {"name": "陕西省", "value": [37327379, 2.32, "陕西省"]},
            {"name": "广西壮族自治区", "value": [46023761, 2.19, "广西壮族自治区"]},
            {"name": "江西省", "value": [44567797, 2.16, "江西省"]},
            {"name": "天津市", "value": [12938693, 2.11, "天津市"]},
            {"name": "山西省", "value": [35712101, 2.11, "山西省"]},
            {"name": "吉林省", "value": [27452815, 1.98, "吉林省"]},
            {"name": "重庆市", "value": [28846170, 1.81, "重庆市"]},
            {"name": "云南省", "value": [45966766, 1.65, "云南省"]},
            {"name": "新疆维吾尔自治区", "value": [21815815, 1.24, "新疆维吾尔自治区"]},
            {"name": "贵州省", "value": [34748556, 1.05, "贵州省"]},
            {"name": "甘肃省", "value": [25575263, 0.94, "甘肃省"]},
            {"name": "海南省", "value": [8671485	, 0.47, "海南省"]},
            {"name": "宁夏回族自治区", "value": [6301350, 0.39, "宁夏回族自治区"]},
            {"name": "青海省", "value": [5626723, 0.31, "青海省"]},
            {"name": "西藏自治区", "value": [3002165, 0.12, "西藏自治区"]},
        ],
    },
]

time_list = [str(d) + "年" for d in range(2004, 2024)]
total_num = [
    129988,
    130756,
    131448,
    132129,
    132802,
    133450,
    134091,
    134916,
    135922,
    136726,
    137646,
    138326,
    139232,
    140011,
    140541,
    141008,
    141212,
    141260,
    141175,
    140967
]
maxNum = 71854210
minNum = 30
def get_year_chart(year: str):
    map_data = [
        [[x["name"], x["value"]] for x in d["data"]] for d in data if d["time"] == '2010年'
    ][0]
    min_data, max_data = (minNum, maxNum)
    data_mark: List = []
    i = 0
    for x in time_list:
        if x == year:
            data_mark.append(total_num[i])
        else:
            data_mark.append("")
        i = i + 1

    map_chart = (
        Map()
        .add(
            series_name="",
            data_pair=map_data,
            zoom=1,
            center=[130.5, 30.5],
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="" + str(year) + "全国人口数量情况（单位：万人） 数据来源：国家统计局",
                subtitle="",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="light"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=JsCode(
                    """function(params) {
                    if ('value' in params.data) {
                        return params.data.value[2] + ': ' + params.data.value[0];
                    }
                }"""
                ),
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="30",
                pos_top="center",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    line_chart = (
        Line()
        .add_xaxis(time_list)
        .add_yaxis("", total_num)
        .add_yaxis(
            "",
            data_mark,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="全国人口数量2004-2023年（单位：万人）", pos_left="72%", pos_top="5%"
            )
        )
    )
    grid_chart = (
        Grid()
        .add(
            line_chart,
            grid_opts=opts.GridOpts(
                pos_left="65%", pos_right="80", pos_top="10%", pos_bottom="50%"
            ),
        )
        .add(map_chart, grid_opts=opts.GridOpts())
    )

    return grid_chart


if __name__ == "__main__":
    timeline = Timeline(
        init_opts=opts.InitOpts(width="100%", height="1200px", theme=ThemeType.DARK)
    )
    for y in time_list:
        g = get_year_chart(year=y)
        timeline.add(g, time_point=str(y))

    timeline.add_schema(
        orient="vertical",
        is_auto_play=True,
        is_inverse=True,
        play_interval=5000,
        pos_left="null",
        pos_right="5",
        pos_top="20",
        pos_bottom="20",
        width="60",
        label_opts=opts.LabelOpts(is_show=True, color="#ddd"),
    )

    timeline.render("Page.html")

"""
from pyecharts.charts import Line
import pyecharts.options as opts
from pyecharts.faker import Faker

line1 = (
    Line(init_opts=opts.InitOpts(width="800px", height="600px"))
        .add_xaxis(Faker.choose())
        .add_yaxis('数据1', Faker.values())
        .add_yaxis('数据2', Faker.values())
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Line 图", title_textstyle_opts=opts.TextStyleOpts(font_size=25)))
)
line1.render('pyecharts-line.html')
"""

from pyecharts.charts import Pie
import pyecharts.options as opts
from pyecharts.faker import Faker

p = (
    Pie(init_opts=opts.InitOpts(width="800px", height="800px"))
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie 设置颜色"))
        # .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)
p.render(path="Bing1.html")

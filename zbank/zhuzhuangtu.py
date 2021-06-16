#coding:utf8
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
from matplotlib.font_manager import FontProperties
 
 
#设置中文字体
font_set = FontProperties(fname = r"E:/project_code/py3_project/simfang.ttf")
 
#设置生成图片的分辨率
matplotlib.rcParams['figure.figsize']
matplotlib.rcParams['savefig.dpi']
 
 
# plt.rcParams['font.sas-serig']=['simfang']
# plt.rcParams['axes.unicode_minus']=False
 
n_groups = 5
 
# means_men = (20, 35, 30, 35, 27)
 
# means_women = (25, 32, 34, 20, 25)
 
#简单数据
sabf = (27,53,81,103,138)

sa = (29,57,89,113,141)

ffd = (30,63,94,119,152)
 
fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.2
 
opacity = 0.4
error_config = {'ecolor': '0.3'}
 
 
rects1 = ax.bar(index, sabf, bar_width,
                alpha=opacity, color='b',
                error_kw=error_config,
                label='SABF')
 
rects2 = ax.bar(index + bar_width, sa, bar_width,
                alpha=opacity, color='m',
                error_kw=error_config,
                label='SA')
 
rects3 = ax.bar(index + bar_width + bar_width, ffd, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label='FFD')
 
ax.set_xticks(index + 3 * bar_width / 3)
ax.set_xticklabels(('100', '200', '300', '400', '500'))
ax.legend()
plt.xlabel(u"数量", fontproperties=font_set)
plt.ylabel(u'数量', fontproperties=font_set)
 
fig.tight_layout()
plt.savefig('result.png', dpi=200)
plt.show()

#-*- coding: UTF-8 -*- 
'''


@author: yhp
'''

from mailmerge import MailMerge
import datetime
from getPGData import getPGData
import setting
#从数据库获取需要展示的内容
exe_sql='''select t.loc_desc,
to_char(t1.job_st_tm,'yyyy/mm/dd hh24:mi'),
to_char(t1.job_ed_tm,'yyyy/mm/dd hh24:mi'),
date_part('hour',(t1.job_ed_tm-t1.job_st_tm))::varchar
 from etl.job_loc t ,etl.job_log t1 
 where t.loc_id=t1.loc_id'''

template = setting.template_dir
 
# 创建邮件合并文档并查看所有字段
etl_dt=datetime.datetime.now().strftime("%Y/%m/%d")
start_time=datetime.datetime.now().strftime("%H:%M:%S")
end_time=datetime.datetime.now().strftime("%H:%M:%S")
#列表
default_time=datetime.datetime.now().strftime("%H:%M:%S")

list_data=getPGData(exe_sql)


document_1 = MailMerge(template)
print(document_1.get_merge_fields())
document_1.merge(
                etl_dt=etl_dt,
                run_status=u"正常",
                start_time=start_time,
                end_time=end_time,
                cost_time="12"
    )
document_1.merge_rows('mod', list_data)
document_1.write(setting.daily_report_dir)

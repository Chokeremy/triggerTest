
# 打印*花
N = '*' * 50

# trigger数据流接口url
URL = 'http://172.16.1.2:38235/api/trigger/Trigger?dataSource=ETL'

# 数据库连接信息
DATABASE_NAME = 'hdr_bank'
USER = 'postgres'
PASSWORD = '765@#sy666'
HOST = '172.16.1.2'
PORT = 5432

# 数据库查询符合条件的患者patient_id，visit_id触发trigger数据流接口
# VTE   62 - 骨科  144 - 泌尿外科  266 - 产科
# SQL = 'select patient_id, visit_id, source_visit_id from visit.visit_record where dept_id = 144 and out_time isnull limit 1 ;'
SQL = 'select patient_id, visit_id, source_visit_id from visit.visit_record where dept_id = 62 and out_time isnull;'
# SQL = 'select patient_id, visit_id, source_visit_id from visit.visit_record where dept_id = 62 and out_time isnull limit 1000; '
# SQL = 'select patient_id, inpat_id, source_inpat_id from visit.inpat_record where current_dept_id = 62 and out_time isnull limit 1000;'

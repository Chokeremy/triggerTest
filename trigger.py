from config import *
from database import PgsqlConnect
import requests
from datetime import datetime


class TriggerRequest:
    """请求trigger接口"""

    def __init__(self):

        # 调用PgsqlConnect.execute_sql方法获取执行sql后的[()]型的数据
        self.json = PgsqlConnect(DATABASE_NAME, USER, PASSWORD, HOST, PORT, SQL).execute_sql()

        # 遍历所有数据，提取(patient_id, visit_id)数据组装发送请求打印返回结果
        for patient in self.json:
            try:
                params = [
                    {
                        "patientId": patient[0],
                        "visitId": patient[1],
                        "tag": "cdss"
                    }
                ]

                # 发送post请求
                self.response = requests.post(url=URL, json=params)

                # 打印返回结果
                print('Trigger接口返回结果：{}\tVisitId：{}\tSourceVisitId：{}\t请求时间：{}'.
                      format(self.response.json()['data'][2:-16], patient[1], patient[2], datetime.now()))
            except Exception as e:
                print(e)

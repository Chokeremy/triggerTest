from json.tool import main
from threading import main_thread
from trigger import TriggerRequest
from trigger import N


class TriggerTest:
    """执行类"""

    def __init__(self):

        print(N + '开始批量执行/api/trigger/Trigger数据流触发接口' + N)
        TriggerRequest()

    def __del__(self):

        print(N + '结束批量执行/api/trigger/Trigger数据流触发接口' + N)


if __name__ == '__main__':

    TriggerTest()

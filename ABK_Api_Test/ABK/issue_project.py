# coding=utf-8
from scripts.http_request_class import HttpRequest
from scripts.get_cfg import ConfigClass


# 分配任务
def issue_batch():

    config = ConfigClass('C:\\Users\\Administrator\\PycharmProjects\\ABK_Api_Test\\ABK\\sid.cfg')
    user_id = config.get_value('id', 'prod_user_id')

    banch_id_01 = config.get_value('banchId', 'banch_id')
    data = {"batchId": banch_id_01,
            "data":
                [
                    {"userid": user_id,
                     "isFree": False,
                     "count": 1
                     }
                ]
            }

    url = config.get_value('url', 'prod_issue_url')
    sid = config.get_value('sid', 'user_sid')
    header = {'sid': sid}
    http = HttpRequest()
    res = (http.get_method('post', url, data=data, is_json=True, headers=header))['rt']['status']

    if res == 200:
        print('分配成功')
    else:
        print('分配失败')


issue_batch()

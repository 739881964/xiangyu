# coding=utf-8
from scripts.http_request_class import HttpRequest
# import json
import random
from scripts.get_cfg import ConfigClass


def create_batch():

    config = ConfigClass('C:\\Users\\Administrator\\PycharmProjects\\ABK_Api_Test\\ABK\\sid.cfg')
    batch_name = 'yxTestBatch' + str(random.randint(2019, 200019))

    task_id = config.get_value('task_id', 'task_id')
    json_data_03 = {"public": {
        "pickBatchId": None,
        "pickTaskId": None,
        "batchId": "",
        "edit": False,
        "taskName": "测试专用-分段重点语句-0507",  # 任务名
        "taskId": task_id,  # 任务Id
        "batchName": batch_name,  # 随机批次名
        "rule": "<p>yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001"
                "yxTest001yxTest001yxTest001yxTest001yxTest001yxTest001yxTes</p>",
        "level": 2,
        "type": 0
    },
        "custom": {
        "base": {
            "batchEdit": False,
            "tagInfo": {
                "cname": "",
                "ename": ""
            },
            "info": {
                "languageType": "error-prone-words",
                "languageList": [
                    {
                        "filename": "易错词",
                        "key": "error-prone-words",
                        "fileId": 1542682949407
                    },
                    {
                        "filename": "备忘录",
                        "key": "1",
                        "fileId": 1541755143433
                    },
                    {
                        "filename": "英文校验",
                        "key": "EnglishDict",
                        "fileId": 1529921039731
                    },
                    {
                        "filename": "口语-书面语 ",
                        "key": "spoken-written",
                        "fileId": 1542682985745
                    },
                    {
                        "filename": "普通话",
                        "key": "普通话",
                        "fileId": 1551351949459
                    },
                    {
                        "filename": "短语流普通话",
                        "key": "putonghua",
                        "fileId": 1552278613769
                    },
                    {
                        "filename": "卫藏-易错词",
                        "key": "error-prone-words-weizang",
                        "fileId": 1554344434970
                    },
                    {
                        "filename": "卫藏-口语书面语",
                        "key": "spoken-written-weizang",
                        "fileId": 1554344419181
                    },
                    {
                        "filename": "char",
                        "key": "dyzPinYin",
                        "fileId": 1561359218187
                    },
                    {
                        "filename": "四川话词典",
                        "key": "sichuanhua",
                        "fileId": 1563356364314
                    },
                    {
                        "filename": "粤语词典",
                        "key": "yueyu",
                        "fileId": 1563356398163
                    },
                    {
                        "filename": "闽南语词典",
                        "key": "minnanyu",
                        "fileId": 1563356439601
                    }
                ]
            },
            "tagBox": False,
            "layerBox": True,
            "layerstatus1": True,
            "layerstatus2": True,
            "layerstatus3": True,
            "importType": 0,
            "importBox": False,
            "importStatus": True,
            "fileList": [],
            "myrid": "9F6A7A95BA2540BEA6E8A19E56C0ACFD600D8922767442A69BFABB1F49E2FB2F",  # 云盘文件rid
            "selectTree": [],
            "selectFileRid": "",
            "selectFileName": "英文3条数据",  # 云盘文件名
            "chooseType": 1,
            "checkedReg": False,
            "checkStatus": True,
            "checkType": 2,
            "checkVal": "55",
            "testStatus": True,
            "testType": 2,
            "testVal": "55",
            "exchangeStatus": True,
            "exchangeVal": 1,
            "textareaStatus": 0,
            "textareaValue": "",
            "recycleTime": 172800
        },
        "spec": {
            "checkStatus": True,
            "checkType": 2,
            "checkVal": "55",
            "testStatus": True,
            "testType": 2,
            "testVal": "55",
            "exchangeStatus": True,
            "exchangeVal": 1,
            "textareaStatus": 0,
            "textareaValue": "",
            "score": {
                "mark": {
                    "coe": "0.1",
                    "formula": "0.1*总条数*正确率",
                    "during": True,
                    "correct": True,
                    "max": 10,
                    "min": 1,
                    "correctWeight": {
                        "textWeight": 0.6,
                        "sentenceWeight": 0.4
                    }
                },
                "check": {
                    "coe": "0.1",
                    "formula": "0.1*总条数",
                    "during": True,
                    "isCheckConfidenceWord": False,
                    "min": 1,
                    "max": 10
                }
            },
            "textLabel": {
                "label": [
                    {
                        "cname": "text"
                    }
                ],
                "isOpen": True
            },
            "chapters": {
                "label": [
                    {
                        "cname": "不可用",
                        "ename": "useless"
                    },
                    {
                        "cname": "独白类",
                        "ename": "du"
                    },
                    {
                        "cname": "对话类",
                        "ename": "ce"
                    }
                ],
                "isOpen": True
            },
            "keySentence": {
                "label": [
                    {
                        "cname": "重点句",
                        "ename": "zhongdianju"
                    },
                    {
                        "cname": "自然段",
                        "ename": "ziranduan"
                    }
                ],
                "isOpen": True
            },
            "timeLabel": {
                "label": [
                    {
                        "cname": "环境噪音",
                        "ename": "noise"
                    },
                    {
                        "cname": "听不清",
                        "ename": "deaf"
                    },
                    {
                        "cname": "静音",
                        "ename": "sil"
                    },
                    {
                        "cname": "混读",
                        "ename": "overlap"
                    },
                    {
                        "cname": "人声噪音",
                        "ename": "side-speech"
                    },
                    {
                        "cname": "时间",
                        "ename": ""
                    },
                    {
                        "cname": "错误",
                        "ename": "error"
                    }
                ],
                "isOpen": True
            },
            "tagListArr": [],
            "tagBox": False,
            "isLabelAttr": False,
            "tagInfo": {
                "cname": "",
                "ename": ""
            },
            "modalStyle": {
                "width": "1928px",
                "height": "1117px",
                "background": "rgba(0,0,0,0.3)",
                "position": "fixed",
                "top": 0,
                "left": 0,
                "zIndex": 9999
            },
            "must": False,
            "multi": False,
            "curType": "textLabel",
            "totalWeight": 1,
            "textLength": 50,
            "checkRule": {
                "chapterLength": 200,  # 自然段字数限制
                "chapterType": 1,
                "paraLength": 1000,  # 分段字数限制
                "paraType": 1,
                "keySentenceRate": 500,  # 重点句出现的频率
                "submitType": 2,  # 1.仅提醒 2.限制提交
                "typeList": [
                    {
                        "name": "自然段字数检错",
                        "type": 1,
                        "isCheck": True
                    },
                    {
                        "name": "篇幅字数检错",
                        "type": 2,
                        "isCheck": True
                    },
                    {
                        "name": "段末标点检错",
                        "type": 3,
                        "isCheck": True
                    },
                    {
                        "name": "重点语句标点检错",
                        "type": 4,
                        "isCheck": True
                    },
                    {
                        "name": "重点语句频率检错",
                        "type": 5,
                        "isCheck": True
                    }
                ]
            },
            "hasVideo": True,
            "enText": False
        }
    }
        }

    config = ConfigClass('C:\\Users\\Administrator\\PycharmProjects\\ABK_Api_Test\\ABK\\sid.cfg')
    sid = config.get_value('sid', 'user_sid')
    _header = {'sid': sid}
    _url = config.get_value('url', 'create_batch_prod_url')

    http = HttpRequest()
    re = (http.get_method('post', _url, data=json_data_03, is_json=True, headers=_header))['data']

    print(re)


create_batch()

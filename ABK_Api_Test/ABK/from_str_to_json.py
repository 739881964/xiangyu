# coding=utf-8
import json


json_data = ''
res_01 = json.dumps(json.loads(json_data), indent=4, sort_keys=False, ensure_ascii=False)

print(res_01)

# with open('json.txt', 'w') as f:
#     json.dump(res, f)


# with open('json.txt', 'r', encoding='utf-8') as f:
#     res = json.load(f, )
#     print(res)

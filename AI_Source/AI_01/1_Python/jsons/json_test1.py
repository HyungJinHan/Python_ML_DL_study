import json

jsonData = """
{
    "snapshot" : {
        "repos" : "test.com/repositories/snapshots",
        "id" : "hhj",
        "pw" : "1210"
    },
    "release" : {
        "repos" : "test.com/repositories/release",
        "id" : "han",
        "pw" : "1210"
    },
    "component" : {
        "test" : "test.com"
    }
}
"""

data_json = json.loads(jsonData) # json 형식의 문자열을 파이썬의 타입으로 변경
print(type(data_json))
print(data_json)
print(data_json['component']['test'])
# <class 'dict'>
# {
#   'snapshot': {'repos': 'test.com/repositories/snapshots', 'id': 'hhj', 'pw': '1210'},
#   'release': {'repos': 'test.com/repositories/release', 'id': 'han', 'pw': '1210'},
#   'component': {'test': 'test.com'}
# }

# data_str = json.dumps(data_json) # json 형식의 데이터를 문자열 형태로 변경
data_str = json.dumps(data_json, indent=4) # 들여쓰기 적용
print(type(data_str))
print(data_str)
# <class 'str'>
# {
#   "snapshot": {"repos": "test.com/repositories/snapshots", "id": "hhj", "pw": "1210"},
#   "release": {"repos": "test.com/repositories/release", "id": "han", "pw": "1210"},
#   "component": {"test": "test.com"}
# }
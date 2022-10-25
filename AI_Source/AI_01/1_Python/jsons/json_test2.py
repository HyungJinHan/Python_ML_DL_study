import json

JSON_FILE = 'json_info.json'
JSON_DATA = {}

def read_json(filename):
    f = open(filename, 'rt')
    # f = open(filename, 'rt', encoding='utf-8')
    js = json.loads(f.read())
    f.close()
    return js

def proc_json():
    global JSON_FILE
    global JSON_DATA
    JSON_DATA = read_json(JSON_FILE)

    repos_1 = JSON_DATA['snapshot']['repos']
    id_1 = JSON_DATA['snapshot']['id']
    pw_1 = JSON_DATA['snapshot']['pw']

    repos_2 = JSON_DATA['release']['repos']
    id_2 = JSON_DATA['release']['id']
    pw_2 = JSON_DATA['release']['pw']

    print('repos_1 value :' + repos_1)
    print('id_1 value : ' + id_1)
    print('pw_1 value : ' + pw_1)
    print()
    print('repos_2 value :' + repos_2)
    print('id_2 value : ' + id_2)
    print('pw_2 value : ' + pw_2)

if __name__ == '__main__':
    proc_json()
    # repos_1 value :test.com/repositories/snapshots
    # id_1 value : hhj
    # pw_1 value : 1210
    #
    # repos_2 value :test.com/repositories/release
    # id_2 value : han
    # pw_2 value : 1210
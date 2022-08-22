import os
import json

#####file write############
# path = os.path.join(os.path.dirname(__file__), 'test.txt')
# f = open(path, 'w', encoding='UTF-8')

# f.write('こんにちはs\n')

# datalist = ['お元気站615552Nonですか？\n', 'それではまた\n']
# f.writelines(datalist)

# f.close()
#####file write############

#####JSON Read e############
path = os.path.join(os.path.dirname(__file__), 'jsondata.json')
json_open = open(path, 'r')
json_load = json.load(json_open)

print(json_load)
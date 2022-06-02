import os

path = os.path.join(os.path.dirname(__file__), 'test.txt')
f = open(path, 'w', encoding='UTF-8')

f.write('こんにちはs\n')

datalist = ['お元気站615552Nonですか？\n', 'それではまた\n']
f.writelines(datalist)

f.close()


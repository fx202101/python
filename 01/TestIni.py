import configparser
import os

#相対パスの取得できなため、OSコマンドを使ってうまくいけます

config = configparser.ConfigParser()
path = os.path.join(os.path.dirname(__file__), 'test.ini')
config.read(path)

print(config.sections())
print(config['TEST']['TEST_KEY1'])


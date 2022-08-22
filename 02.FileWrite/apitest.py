import sys


def main():
    print("------------")
    commt ='''
        1:時間間隔
        2:実行時間
        3:お届け日
        その他：管理法人コード：001　前回問い合わせ日時：Nullでデフォルト値として設定される。
    '''
    if(len(sys.argv) <= 1):
        print('You need args!')
        print(commt)
        return 
    args = sys.argv    
    #print(args[1])


if __name__ == '__main__':
    main()
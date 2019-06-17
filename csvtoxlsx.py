"""
twiport(http://twport.com)から取得したcsvファイルをxlsxに変換
ついでに指定した数字から乱数をだすプログラム

14行目でcsvファイルの名前をキャンペーンごとに指定必要

2019.05.27
"""
import pandas as pd
import random

pd.set_option('display.max_rows', None)
#twportで作成したcsvファイルを記入
df = pd.read_csv('twport_84750.csv')  
#csvをxlsxにエンコード
df.to_excel('RTcampaign.xlsx', encoding='utf-8')

#引数に最大数を渡して、1~渡した引き数の間から数字をランダムで返す関数
def choice(max):
    num = random.randint(0,max)
    print(num)

#for文のrenge内に抽選人数,choice()にキャンペーンの人数を入力
for i in range(5):
    choice(6058)

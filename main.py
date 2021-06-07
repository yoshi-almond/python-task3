import eel
import pandas as pd
import os
import sys
from os import chdir
from os.path import dirname
from sys import executable

@eel.expose
def py_search(word,name):
    if getattr(sys, 'frozen', False):
        chdir(dirname(executable))
        chdir("../../../../")
    cdp = os.getcwd()
    csv_path = cdp + "/" + name
    try:
        print(csv_path)
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("ファイルが見つかりません")
        return 0, cdp
    src = list(df['name'])
    if word in src:
        print(word+'が見つかりました')
        return 1, cdp
    else:
        print(word+'は見つかりませんでした')
        src.append(word)
        src = pd.DataFrame(src,columns=['name'])
        src.to_csv(csv_path,index=False)
        print(word+'を新しく追加しました')
        return 2, cdp

eel.init("web") #HTMLのフォルダ
eel.start("main.html") #スタートページのファイル名

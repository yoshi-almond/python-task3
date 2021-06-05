import eel
import pandas as pd
import os

@eel.expose
def py_search(word,path):
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print("ファイルが見つかりません")
        return 0
    src = list(df['name'])
    if word in src:
        print(word+'が見つかりました')
        return 1
    else:
        print(word+'は見つかりませんでした')
        src.append(word)
        src = pd.DataFrame(src,columns=['name'])
        src.to_csv(path,index=False)
        print(word+'を新しく追加しました')
        return 2

eel.init("web") #HTMLのフォルダ
eel.start("main.html") #スタートページのファイル名



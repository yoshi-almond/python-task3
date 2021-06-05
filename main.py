import eel
import pandas as pd
import os
import sys

@eel.expose
def py_search(word,name):
    if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
        dpath = sys._MEIPASS
    else:
        dpath = os.path.dirname(os.path.abspath(__file__))
    print(dpath)
    csv_path = dpath + '/' + name
    try:
        print(csv_path)
        df = pd.read_csv(csv_path)
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
        src.to_csv(csv_path,index=False)
        print(word+'を新しく追加しました')
        return 2

eel.init("web") #HTMLのフォルダ
eel.start("main.html") #スタートページのファイル名

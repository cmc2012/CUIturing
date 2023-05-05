'''
                  江城子 . 程序员之歌

              十年生死两茫茫，写程序，到天亮。
                  千行代码，Bug何处藏。
              纵使上线又怎样，朝令改，夕断肠。

              领导每天新想法，天天改，日日忙。
                  相顾无言，惟有泪千行。
              每晚灯火阑珊处，夜难寐，加班狂。

'''

print("欢迎使用CUITuring程序答疑解难")
actid=int(input("输入1检查依赖库"))
import json,os
if(actid==1):
    '''
    以下判断及捕捉都是答辩
    '''
    lack=[]
    try:
        import asyncio
    except:
        lack.append("asyncio")
    try:
        import urllib3
    except:
        lack.append("urllib3")
    try:
        import git
    except:
        lack.append("gitpython")
    try:
        import turingAPI
    except:
        with open("settings.ini","r") as load_file:
            settings=load_file.read()
            load_file.close()
        psettings=json.loads(settings)
        if(psettings["full-version"]==False):
            try:
                os.scandir("Lib")
                print("您的程序包含turingAPI,请在settings.ini中开启full-version项")
            finally:
                lack.append("turingAPI")
    try:
        import aiohttp
    except:
        lack.append("aiohttp")
    try:
        import keyboard
    except:
        lack.append("keyboard")
    if(lack==[]):
        print("您的程序不缺少支持库!")
    else:
        print("您的程序缺少",end="")
        for x in lack:
            print(x+" ",end="")
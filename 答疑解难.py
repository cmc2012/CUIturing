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
if(actid==1):
    '''
    以下判断及捕捉都是答辩
    '''
    try:
        import os
    except:
        print("os缺少!")
    try:
        import asyncio
    except:
        print("asyncio缺少!")
    try:
        import urllib3
    except:
        print("urllib3缺少!")
    try:
        import git
    except:
        print("gitpython缺少!")
    try:
        import gitdb
    except:
        print("gitdb缺少!")
    try:
        import turingAPI
    except:
        try:
            os.scandir("Lib")
            print("您的程序包含turingAPI,请在settings.ini中开启full-version项")
        except:
            print("turingAPI缺少!")
    try:
        import aiohttp
    except:
        print("aiohttp缺少!")
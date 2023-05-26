import Tools.Download_project
import colorama
import json
import os
import Lib.turingAPI as turingAPI


def tools():
    print(colorama.Back.LIGHTRED_EX + colorama.Fore.BLACK + "===========Tools===========")
    print("(1)下载项目")
    print("输入e退出")
    actionId = input()
    try:
        actionId = int(actionId)
    except:
        if (actionId == "e"):
            return 0
        else:
            print("无效的动作id")
    if (actionId == 1):
        projectPath = input()
        Tools.Download_project.get_project("https://icode.youdao.com/scratch/project/" + user.getWorkId(projectPath),user.getWorkDetail(user.getWorkId(projectPath), 1)["title"])
    tools()
def menu(num):
    try:
        num = int(num)
    except:
        if (num == "e"):
            return 0
        else:
            print("无效的动作id")
    if (num == 0):
        tools()
    if (num == 1):
        works=user.getWorks(1,100,2,isParse=1)
        works=json.dumps(works)
        print(works)
def saveCookie(cookie):
    with open("cookie.txt","w") as file:
        file.write(cookie)
def readcookie():
    with open("cookie.txt","r") as file:
        return file.read()

colorama.init(autoreset=True)
with open("settings.json", "r") as load_file:
    settings = load_file.read()
    load_file.close()
psettings = json.loads(settings)
if(not(os.path.exists("cookie.txt"))):
    cookie = input("请输入cookie\n")
    saveCookie(cookie)
print("登陆中")
user = turingAPI.icodeUser(readcookie())
if (not (user.isLogin)):
    if(os.path.exists("cookie.txt")):
        cookie = input("请输入cookie\n")
        saveCookie(cookie)
        print("请重启程序!")
    print(colorama.Fore.RED + "cookie is invalid")
    exit(-1)
print(colorama.Fore.GREEN + "登录完成")
while (True):
    num=input()
    menu(num)

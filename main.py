import json,os
have_settings=os.path.isfile(".//settings.ini")
setting=open(".//settings.ini")
if(not(have_settings)):
    setting.write("")
import turingAPI
import urllib3
cookie=input("cookie:")
print("Logging...")
user=turingAPI.icodeUser(cookie)
print("Login is successfully.")
if(not(user.checkLogin())):
    print("cookie is invalid")
    exit(1)
print("小图灵控制台版登陆成功，请输入功能编号")
'''
_______________#########_______________________ 
______________############_____________________ 
______________#############____________________ 
_____________##__###########___________________ 
____________###__######_#####__________________ 
____________###_#######___####_________________ 
___________###__##########_####________________ 
__________####__###########_####_______________ 
________#####___###########__#####_____________ 
_______######___###_########___#####___________ 
_______#####___###___########___######_________ 
______######___###__###########___######_______ 
_____######___####_##############__######______ 
____#######__#####################_#######_____ 
____#######__##############################____ 
___#######__######_#################_#######___ 
___#######__######_######_#########___######___ 
___#######____##__######___######_____######___ 
___#######________######____#####_____#####____ 
____######________#####_____#####_____####_____ 
_____#####________####______#####_____###______ 
______#####______;###________###______#________ 
________##_______####________####______________ 
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
        import urllib3
    except:
        lack.append("urllib3")
    try:
        import git
    except:
        lack.append("gitpython")
    try:
        import colorma
    except:
        lack.append("colorma")
    if(not os.path.exists(".\\Lib")):
        lack.append("turingAPI")
    try:
        import aiohttp
    except:
        lack.append("aiohttp")
    if(lack==[]):
        print("您的程序不缺少支持库!")
    else:
        print("您的程序缺少",end="")
        for x in lack:
            print(x+" ",end="")
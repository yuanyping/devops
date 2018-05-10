from django.shortcuts import render,HttpResponse
from db import models
# Create your views here.

def menu_select(user_name):
    menus=models.UserInfo.objects.filter(user_name=user_name).values("user_menu__id","user_menu__menu_name")   #获取授权的菜单的1级目录
    menu_list_tmp=[]
    for i in menus:
        menu_list_tmp.append(i)
    # print(menu_list_tmp)
    # print(menus)
    menu_list={}
    for menu_i in menu_list_tmp:
        menu=menu_i["user_menu__id"]    #得到id
        menu_name=menu_i["user_menu__menu_name"]    #得到1级目录名字
        sub_menus=models.SubMenu.objects.filter(super_menu=menu).values("sub_menu_name","sub_menu_alias") #通过1级目录获取子目录
        for p in menu_list_tmp:
            if p["user_menu__id"] == menu:
                p["sub_menu"]=sub_menus
    menu_list["menu_list"]=menu_list_tmp
    return menu_list

def login(request):
    global result
    if request.method == "GET":
        if request.session.get("user",None) == None:
            return render(request,"login.html")
        else:
            user_name=request.session.get("user",None)
            menu_list=menu_select(user_name)    #{'sub6': ['添加用户', '用户管理'], 'sub7': ['hgame数据库', 'xgame数据'], 'menu_list': <QuerySet [{'user_menu__id': 6, 'user_menu__menu_name': '用户管理'}, {'user_menu__id': 7, 'user_menu__menu_name': '数据库管理'}]>,}
            result_tmp={"user_name": user_name,}
            result=dict(menu_list,**result_tmp)     #两个字典合并
            print(result)
            return render(request, "welcome.html",result )
    else:
        user_name= request.POST.get("user_name")
        user_pwd = request.POST.get("user_pwd")
        r_me= request.POST.get("r_me")
        check_user=models.UserInfo.objects.filter(user_name=user_name,user_pwd=user_pwd).count()
        if check_user == 1:
            if r_me == "on":
                request.session["user"]=user_name
            else:
                pass
            user_name = request.session.get("user", None)
            menu_list = menu_select(user_name)
            return render(request, "welcome.html", result)
        else:
            return render(request,"login.html",{"info":"登录失败，请重新登录"})

def loginout(request):
    request.session.clear()
    return render(request,"login.html")
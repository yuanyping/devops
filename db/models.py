from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name=models.CharField(max_length=32)
    user_pwd=models.CharField(max_length=32)
    user_menu=models.ManyToManyField(to="Menu")     #给用户授权菜单，只有授权的用户才会看到显示的菜单
    def __str__(self):
        return self.user_name

class Menu(models.Model):
    menu_name=models.CharField(max_length=128)
    def __str__(self):
        return self.menu_name

class SubMenu(models.Model):
    sub_menu_name=models.CharField(max_length=128)
    sub_menu_alias = models.CharField(max_length=128,verbose_name="英文名")
    super_menu=models.ManyToManyField(to="Menu")

    def __str__(self):
        return self.sub_menu_name

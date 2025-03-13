"""为应用程序accounts 定义url模式"""

from django.urls import path, include

from . import views

app_name='accounts'
urlpatterns=[
    #包含身份验证的urls 这是django自带的身份认真
    #自带功能编入accounts下后,只能用这里的app的url访问
    #django的默认视图中有login  所以导向这里会继续寻找这个urls中的函数
    path('',include('django.contrib.auth.urls')),#这个自带的只有login和logout等,直接访问报错因为没有这个对应的视图
    #注册界面
    path('register/', views.register,name='register')
]
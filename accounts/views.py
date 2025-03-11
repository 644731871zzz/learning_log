from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        #显示空的注册表单
        form = UserCreationForm()
    else:
        #根据用户数据处理填写好的表单
        form = UserCreationForm(data=request.POST)
        #检查数据是否有效(没有非法字符,名称重复,恶意名称,确认密码是否相同等)
        if form.is_valid():
            new_user = form.save() #存储用户名,密码的哈希值到数据库,赋值到new_user上
            #让用户自动登录,再重新定向
            login(request,new_user)
            return redirect('learning_logs:index')
        
    #显示空表单或指出表单无效
    #如果用户填写的信息无效,is_valid拒绝了,但是其中的form还包含无效的信息传递给模板显示
    context = {'form': form}
    return render(request,'registration/register.html',context)

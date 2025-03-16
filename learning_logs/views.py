from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic,Entry

from .forms import TopicForm,EntryForm

def index(request):
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')

@login_required
def topics(request):
    """显示所有的主题"""
    #依照已经登录的用户显示
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    """显示单个主题极其所有的条目"""
    topic=Topic.objects.get(id=topic_id)

    #确定请求主题的用户是否关联此主题
    #导入练习19.3定义的函数进行验证
    check_topic_owner(request,topic)
    
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    """添加新的主题"""
    #初次请求发送get请求,返回空表单.填写表单发送post请求
    if request.method != 'POST':
        #未提交数据:创建一个新的表单
        form=TopicForm()
    else:
        #POST 提交的数据:对数据进行处理
        form=TopicForm(data=request.POST)
        #验证数据有效性 is_valid用来核实必要默认字段,并且输入的数据与要求的字段类型一致
        #一些字段的要求是写在models中,将会自动验证
        #字段都有效将会调用save
        if form.is_valid():
            #不立即保存到数据库,先创建表单,但是不提交,仅一次访问数据库
            new_topic = form.save(commit=False)
            new_topic.owner =request.user
            new_topic.save()
            
            #将用户界面重定向跳转
            return redirect('learning_logs:topics')
        
    #显示空表单或之处表单数据无效 如果为get请求将没有实参,是一个空表单
    #没在if中因为不论刚进入界面还是提交的数据无效(wlse中的return没有执行)这里的语句都执行
    #报错会让用户知道
    context={'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    """在特定主题下添加新条目"""
    #获取id
    topic=Topic.objects.get(id=topic_id)

    #检查请求方法是否为POST
    #如果是GET将会创建新的表单
    if request.method != 'POST':
        #未提交数据,提供空表单
        form = EntryForm()
    #如果为POST执行这里的语句
    else:
        #POST提交的数据:对数据进行处理 将POST数据填充进去
        form=EntryForm(data=request.POST)
        #自动验证字段并存储
        if form.is_valid():
            #创建新的对象条目
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id=topic_id)
    
    #显示空表单或者指出表单数据无效
    context={'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic

    #导入练习19.3定义的函数进行验证
    check_topic_owner(request,topic)

    if request.method !='POST':
        #初次请求将使用当前的条目填成标签
        form=EntryForm(instance=entry)
    else:
        #post提交的数据
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
        
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)



def check_topic_owner(request,topic):
    """练习19.3作业,用于验证用户id和配置主题id是否匹配."""
    if topic.owner != request.user:
        #raise直接终止视图返回错误界面 
        # return redirect可能会暴露entry_id是否存在
        # 因为仅仅是跳转,可能知道检查user的函数运行了,id就是访问的id
        raise Http404


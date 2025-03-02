from django.shortcuts import render,redirect
from .models import Topic,Entry

from .forms import TopicForm,EntryForm

def index(request):
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    """显示单个主题极其所有的条目"""
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

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
            form.save()
            #将用户界面重定向跳转
            return redirect('learning_logs:topics')
        
    #显示空表单或之处表单数据无效 如果为get请求将没有实参,是一个空表单
    #没在if中因为不论刚进入界面还是提交的数据无效(wlse中的return没有执行)这里的语句都执行
    #报错会让用户知道
    context={'form':form}
    return render(request,'learning_logs/new_topic.html',context)

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

def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic

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

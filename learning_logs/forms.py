#导入forms 用于处理表单数据
from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        """定义元数据,指定显示内容"""
        model=Topic #指定关联类
        fields=['text']  #指定显示字段
        labels={'text':''}  #指定字段标签,为空表示不会出现默认的字段的标签值

class EntryForm(forms.ModelForm):
    class Meta: #根据指定信息创建表单
        model = Entry
        fields = ['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}
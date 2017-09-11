from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        # 表明这个表单对应的数据库模型是Comment类
        model = Comment
        # 指定了表单需要显示的字段，这里我们指定了name、email、url、text需要显示。
        fields = ['name','email','url','text']

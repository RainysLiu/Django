from django import forms
class User(forms.Form):
    name=forms.CharField(label='用户名',max_length=10)
    passwd=forms.CharField(label='密码',max_length=10)
    email=forms.EmailField(label='邮箱',max_length=20)

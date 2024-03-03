from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    # 이메일 속성을 추가하기 위해 UserCreationForm클래스 상속
    email = forms.EmailField(label="이메일")
     
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
        # 비번 1,2 대조 & 비번 생성 규칙 로직 내부적으로 지님.

from django import forms #forms.pyでは必ずインポートする
from .models import Post #Postテーブルを使う
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'thumbnail')

    # ↓のinitはform-controlで見た目をきれいにしたいだけ。
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class LoginForm(AuthenticationForm):
    # ↓のinitはform-controlで見た目をきれいにしたいだけ。
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class SearchForm(forms.Form):
    freeword = forms.CharField(min_length=1, max_length=30, label='', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        #在注册界面添加邮箱，手机，微信，QQ，地址
        fields = UserCreationForm.Meta.fields + ('email','mobile','address','qq','weChat')
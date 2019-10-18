from django.shortcuts import render

# Create your views here.
from UserApp.models import AxfUser


def mine(request):
    # mine 如何获取登陆的用户名？
    # 两个师徒函数如何传递数据
    user_id = request.session.get('user_id')
    context = {
        'user_id':user_id
    }
    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        context['user']=user


    return render(request,'axf/main/mine/mine.html',context=context)
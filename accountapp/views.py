from django.shortcuts import render
from .models import account
#암호 해쉬 도구 ? api ? 그런거 bcrypt
import bcrypt

def account_pg(request):
    #그냥 페이지 불러 오는듯
    if request.method == 'GET':
        return render(request, 'account_pg.html')
    #여기부터 회원 가입 데이터를 쌓는거
    elif request.method == 'POST':
     #먼가 하는건가?
     res_data ={}
     # account db 변수 설정?
     new_user = account()
     # 요청을 가져옴
     new_user.Username = request.POST.get('Username', None)
     # 암호 해쉬화 변수 저장
     wcpassword = request.POST.get('password', None)
     # 암호 해쉬 화
     hashed_password = bcrypt.hashpw(wcpassword.encode("utf-8"), bcrypt.gensalt())
     # 암호 변수 저장
     new_user.password = hashed_password
     # 이게 저장 하는 것을 의미
     new_user.save()
    # Username = request.Get.get('Username', None)
    # password = request.Get.get('password', None)
    # res_data가 있어야 쌓이는듯?
    return render(request, 'account_pg.html', res_data)
# def register(request):
#      return render(request, 'register.html')

# # Create your views here.
#계정 저장 인듯
# def save(account_pg):
#     Username = account.cleaned_data.get("Username")
#     password = account.cleaned_data.get("password")
#     user = account.User.objects.create_user(Username, password)
#     user.save()


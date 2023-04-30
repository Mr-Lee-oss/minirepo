from django.db import models

# Create your models here.


# class AccountCreate(CreateView):
#     model = User
#     form_class = CreationUserForm
#     success_url = reverse_lazy(성공시 이동 경로)
#     template_name = 데이터 보낼 경로

class account(models.Model):
    Username = models.CharField(max_length=64, verbose_name="사용자 계정")

    password = models.CharField(max_length=64, verbose_name="비밀번호")

    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    class Meta:
        db_table = 'account_user'
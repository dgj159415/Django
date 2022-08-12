# models.py
from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)  # 与数据库表user中的字段名称一致
    username = models.CharField(max_length=150, null=False)  # 与数据库表user中的字段一致
    email = models.CharField(max_length=254, null=False)  # 与数据库表user中的字段一致

    class Meta:
        db_table = 'userinfo'

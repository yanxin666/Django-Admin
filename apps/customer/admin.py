from django.contrib import admin
from .models import CustomerUser

# 注册 CustomerUser 模型到 Django 管理后台
admin.site.register(CustomerUser)

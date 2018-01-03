from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

admin.site.register(Question)   # 配置数据库模块
admin.site.register(Choice)
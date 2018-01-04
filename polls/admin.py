from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice
from django.contrib import admin

from .models import Choice, Question

# admin.site.register(Question)   # 配置数据库模块，让其在admin后台可见
# admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']     # 列表页面过滤器
    search_fields = ['question_text']   # 添加搜索功能


admin.site.register(Question, QuestionAdmin)

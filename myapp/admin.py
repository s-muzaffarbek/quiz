from django.contrib import admin
from .models import Topic, Question, Answer, Result

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']

class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['name', 'is_right']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['name', 'topic']
    list_display = ['name', 'topic']
    inlines = [AnswerInline]

admin.site.register(Result)



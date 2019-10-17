from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Text Information', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
'''class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Escolha', {'fields': ['question''question_text']}),
        ('Date Information', {'fields': ['pub_date']}),'''

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
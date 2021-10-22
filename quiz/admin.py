from django.contrib import admin
from .models import QuizSet, Quiz, Answer

# Register your models here.

@admin.register(QuizSet)
class QuizSetAdmin(admin.ModelAdmin):
  list_display = ['id', 'host', 'created_at']

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
  list_display = ['id', 'quiz_set_id', 'question', 'answer', 'created_at']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
  list_display = ['id', 'quiz_set_id', 'guest', 'points', 'created_at']
  
from django.db import models
from .errors import options_errors, name_errors, answer_errors
from django.core.validators import MinValueValidator, MaxValueValidator

OPTION_CHOICES = (
  (1, '1'),
  (2, '2'),
  (3, '3'),
  (4, '4'),
  (5, '5'),
)
# Create your models here.
class QuizSet(models.Model):
  id = models.AutoField(primary_key=True)
  host = models.CharField(max_length=10, unique=False, verbose_name='퀴즈 낸 사람', error_messages=name_errors)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.id)

class Quiz(models.Model):
  quiz_set_id = models.ForeignKey(QuizSet, on_delete=models.CASCADE, verbose_name='퀴즈 셋 번호')
  question = models.CharField(max_length=100, unique=False, verbose_name='문제', error_messages=options_errors)
  option_1 = models.CharField(max_length=50, unique=False, verbose_name='선택지1', error_messages=options_errors)
  option_2 = models.CharField(max_length=50, unique=False, verbose_name='선택지2', error_messages=options_errors)
  option_3 = models.CharField(max_length=50, unique=False, verbose_name='선택지3', error_messages=options_errors)
  option_4 = models.CharField(max_length=50, unique=False, verbose_name='선택지4', error_messages=options_errors)
  option_5 = models.CharField(max_length=50, unique=False, verbose_name='선택지5', error_messages=options_errors)
  answer = models.IntegerField(verbose_name='정답', error_messages=answer_errors, choices=OPTION_CHOICES)
  created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
  quiz_set_id = models.ForeignKey(QuizSet, on_delete=models.CASCADE, verbose_name='퀴즈 셋 번호')
  guest = models.CharField(max_length=10, unique=False, verbose_name='퀴즈 푼 사람', error_messages=name_errors)
  points = models.IntegerField(verbose_name='정답 개수')
  created_at = models.DateTimeField(auto_now_add=True)
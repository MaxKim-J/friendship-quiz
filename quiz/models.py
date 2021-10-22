from django.db import models

# Create your models here.

class QuizSet(models.Model):
  id = models.AutoField(primary_key=True)
  host = models.CharField(max_length=10, unique=False, verbose_name='퀴즈 낸 사람')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.id)

class Quiz(models.Model):
  quiz_set_id = models.ForeignKey(QuizSet, on_delete=models.CASCADE, verbose_name='퀴즈 셋 번호')
  question = models.CharField(max_length=100, unique=False, verbose_name='문제')
  option_1 = models.CharField(max_length=50, unique=False, verbose_name='선지1')
  option_2 = models.CharField(max_length=50, unique=False, verbose_name='선지2')
  option_3 = models.CharField(max_length=50, unique=False, verbose_name='선지3')
  option_4 = models.CharField(max_length=50, unique=False, verbose_name='선지4')
  option_5 = models.CharField(max_length=50, unique=False, verbose_name='선지5')
  answer = models.IntegerField(verbose_name='정답')
  created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
  quiz_set_id = models.ForeignKey(QuizSet, on_delete=models.CASCADE, verbose_name='퀴즈 셋 번호')
  guest = models.CharField(max_length=10, unique=False, verbose_name='퀴즈 푼 사람')
  points = models.IntegerField(verbose_name='정답 개수')
  created_at = models.DateTimeField(auto_now_add=True)
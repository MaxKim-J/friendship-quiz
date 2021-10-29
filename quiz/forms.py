from django import forms
from .models import Quiz, QuizSet
from .errors import default_errors

class QuizSetForm(forms.ModelForm):
    class Meta:
        model = QuizSet
        fields = ['host']

class AnswerForm(forms.Form):
    pass

QuizFormSet = forms.modelformset_factory(Quiz, fields=('question', 'option_1', 'option_2', 'option_3', 'option_4', 'option_5', 'answer'),extra=7,error_messages=default_errors)
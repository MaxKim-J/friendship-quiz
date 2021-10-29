from django import forms
from .models import Quiz, QuizSet

class QuizSetForm(forms.ModelForm):
    class Meta:
        model = QuizSet
        fields = ['host']

class AnswerForm(forms.Form):
    pass

QuizFormSet = forms.modelformset_factory(Quiz, fields=('question', 'option_1', 'option_2', 'option_3', 'option_4', 'option_5', 'answer'),extra=7,)
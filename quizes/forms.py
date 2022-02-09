from django.forms import ModelForm

from .models import Quiz

class CreateQuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields=['question', 'option_one','option_two','option_three']
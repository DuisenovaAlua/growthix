from django import forms
from django.forms import ModelForm
from .models import Test,User1,User2
class SignUp1Form(ModelForm):
      class Meta:
          model = User1
          fields = ('user','first_name','last_name',)
class SignUp2Form(ModelForm):
      class Meta:
          model = User2
          fields = ('user','email', 'university', 'speciality','checking','score')

class TestForm (ModelForm):
    class Meta:
        model = Test
        fields = ('number','sections','question', 'A', 'B', 'C','answer',)
  
    
	
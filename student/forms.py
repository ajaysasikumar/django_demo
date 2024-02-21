
# forms.py
from django import forms
from .models import StudentInfo,Academics

class MyForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['student_id','name','Class','Place','phone']


class Academic_form(forms.ModelForm):
    class Meta:
        model = Academics
        fields = ['maths', 'physics', 'chemistry', 'computer_science', 'english']


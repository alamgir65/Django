from django import forms 
from firstApp.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name' : 'Student_Name',
            'roll' : 'Student_Id'
        }
        
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'btn-primary'}),
        }
        
        help_texts = {
            'name' : 'Enter Student Name',
        }
        error_messages = {
            'name' : {'required' : 'Your name must be at least'}
        }
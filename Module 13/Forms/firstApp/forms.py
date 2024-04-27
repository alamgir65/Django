from django import forms
from django.core import validators

# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label = "User Name", help_text='Name within 20 characters only', 
                           widget=forms.Textarea(attrs={'id' : 'nameee', 'placeholder':'Enter your name'}))
    # email = forms.EmailField(label = "User Email")
    
    # file = forms.FileField()
    # img = forms.ImageField()
    
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    # birthday = forms.DateField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    # appoinment = forms.DateTimeField()
    appoinment = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    # Agree = forms.BooleanField()
    
    
    LIST = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=LIST , widget=forms.RadioSelect)
    
    MEAL = [('P', 'Pepparoni'), ('M', "Mashroom"), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    
# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    
    # Validations Name with long process
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 6:
    #         raise forms.ValidationError('Please enter at least six characters!')
    #     else:
    #         return valname

    
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Please Email must contain .com')
    #     return valemail
    
    # Validations Shortcut 
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = cleaned_data['name']
    #     valemail = cleaned_data['email']
    #     if len(valname) < 6:
    #         raise forms.ValidationError('Name must be at least 6 characters')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Email must Contains .com')
    
    

# ==== Django Built-in Validators ====
def check_validators(value):
    if len(value) < 6:
        raise forms.ValidationError('Name must be at least 6 characters')

class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput , validators=[validators.MinLengthValidator(6,message='Please Enter at least 6 characters')])
    
    email = forms.CharField(widget=forms.EmailInput , validators=[validators.EmailValidator(message='Enter a valid email')])
    
    Age = forms.IntegerField( validators=[validators.MaxValueValidator(60 , message='You are now very old marriage is only for young man') , validators.MinValueValidator(21,'You are very small child')])
    
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message='Allow only pdf')])
    
    text = forms.CharField(widget=forms.TextInput , validators=[check_validators])
    
    
class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_repass = self.cleaned_data['confirm_password']
        if val_repass != val_pass:
            raise forms.ValidationError('Passwords does not match')
    

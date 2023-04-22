from django import forms
from .models import Client, Lawyer, Case



# CREATE FORMS FOR MODELS

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name","last_name","email", "phone"]

class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ["first_name","last_name","email", "phone"]    
        
class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ["title","description","status", "client","lawyer"]      



'''
In Django, Class Meta: is a special inner class that can be used in class-based views,
 models, and forms to provide additional information about the class and its behavior.

The Class Meta: inner class can be used to specify options such as:

The database table name for a model
The ordering of querysets
The default ordering of form fields
The form field labels and help texts
The available choices for a choice field
The model fields to exclude or include in a form

Class Meta: is a powerful tool in Django that enables developers to customize 
the behavior of class-based views, models, and forms by providing additional 
options and settings.


'''           
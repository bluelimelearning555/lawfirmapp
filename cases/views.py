'''
from django.shortcuts import render is a Python statement that 
imports the render function from the django.shortcuts module in Django.

'''

from django.shortcuts import render

# IMPORT GENERIC VIEWS

from django.views.generic import ListView, CreateView,UpdateView,DeleteView,TemplateView

# IMPORT MODELS FROM MODELS.PY FILE IN DJANGO APP and form models from  forms.py

from .models import Client, Lawyer ,Case

from .forms import ClientForm , LawyerForm , CaseForm

# IMPORT REVERSE LAZY
from django.urls import reverse_lazy


#from datetime import datetime

# CREATE YOUR VIEWS HERE

# Note Class views have their first letter of each word capitalized
# Template View already contains all the logic required to display our template,
# just specify template name
# In Django, success_url is a property that can be set in a class-based view to
# specify the URL to which the user should be redirected after a successful form submission.

'''
reverse_lazy is used to lazily reverse the URL, which means
that the URL is not resolved until it is needed.
This is useful when using the success_url property 
because the URL may not be available at the time the view is loaded.

self is a fundamental concept in object-oriented programming,
including Django. It provides a way to access instance-level variables
and methods and to refer to the current instance of a class or object.

self is a reference to the current instance of a class or object. 
It is used to access the properties and methods of the instance, including those
inherited from parent classes.

**kwargs is a special parameter in a function or method that allows passing an
arbitrary number of keyword arguments. The ** before kwargs is the "unpacking" operator
 that converts the keyword arguments passed to the function into a dictionary.

 Using **kwargs is a way to make a function more flexible and extensible, as it
 allows callers to pass additional keyword arguments that the function may not explicitly define.
 The function can then process the keyword arguments as needed using Python's dictionary methods.

 It allows callers to pass arbitrary keyword arguments to a 
function, which can then be processed and used as needed.

super() is a built-in function that is used to call a method in a parent class.
 It is often used in Python's object-oriented programming paradigm to enable 
 inheritance and override methods in subclasses.



'''
# CREATE HOMEPAGE VIEW

class HomeView(TemplateView):
    template_name = "home.html"


# CREATE CLIENT VIEWS

class ClientListView(ListView):
    model = Client
    template_name = "clients/client_list.html"


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = "clients/client_form.html"
    success_url = "/clients/"


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "clients/client_form.html"
    success_url = "/clients/"


class ClientDeleteView(DeleteView):
    model = Client    
    template_name = "clients/client_confirm_delete.html"
    success_url = reverse_lazy("cases:client_list")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Client"
        return context


 # CREATE LAWYER VIEWS
 
class LawyerListView(ListView):
    model = Lawyer
    template_name = "lawyers/lawyer_list.html"


class LawyerCreateView(CreateView):
    model = Lawyer
    form_class = LawyerForm
    template_name = "lawyers/lawyer_form.html"
    success_url = "/lawyers/"


class LawyerUpdateView(UpdateView):
    model = Lawyer
    form_class = LawyerForm
    template_name = "lawyers/lawyer_form.html"
    success_url = "/lawyers/"
   

 
class LawyerDeleteView(DeleteView):
    model = Lawyer  
    template_name = "lawyers/lawyer_confirm_delete.html"
    success_url = reverse_lazy("cases:lawyer_list")


# CREATE CASE VIEWS


class CaseListView(ListView):
    model = Case
    template_name = "cases/case_list.html"


class CaseCreateView(CreateView):
    model = Case
    form_class = CaseForm
    template_name = "cases/case_form.html"
    success_url = "/cases/"


class CaseUpdateView(UpdateView):
    model = Case
    form_class = CaseForm
    template_name = "cases/case_form.html"
    success_url = "/cases/"
   

 
class CaseDeleteView(DeleteView):
    model = Case    
    template_name = "cases/case_confirm_delete.html"
    success_url = reverse_lazy("cases:case_list")

'''
def current_year(request):
    now = datetime.datetime.now()
    context = {'now': now}
    return render(request,'current_year.html',content)
'''

'''
class CurrentYearView(TemplateView):
    template_name = 'current_year.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.datetime.now()
        return context
'''        
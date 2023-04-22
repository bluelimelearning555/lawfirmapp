'''
This is a Python import statement that imports the path function
from the django.urls module. The path function is used to define 
URL patterns in Django.

The path function takes two required arguments: a string 
representing the URL pattern, and a view function that will be 
called when the URL pattern is matched.

The path function can also take optional arguments, such as name, 
kwargs, and defaults, to further customize the URL pattern.

The path function is a commonly used function in Django 
for defining URL patterns, along with other functions such as re_path, 
include, and reverse.


urlpatterns is a list of URL patterns in Django, defined in the
urls.py module of each Django app. Each URL pattern is a tuple 
that contains a regular expression (regex) string and a view function 
that will be called when the URL pattern is matched.

URL pattern that matches the root URL ('') of the app,
and calls the home function in the views.py file to handle the request.

We also specify a name for this URL pattern (name='home'), 
which can be used to reference the URL in templates
or views using the {% url %} template tag or the reverse() function.

<int:pk> captures an integer value for pk, which is passed to the 
view as a named parameter. When this URL is requested, 
the  view will be called to handle the request.


DO NOT FORGET TO UPDATE THE PROJECT'S URL'S TO INCLUDE THE URLS  FROM THE APPS



'''



from django.urls import path
from . import views

app_name = "cases"

urlpatterns = [
	# DEFINE URL FOR HOME PAGE
	path("", views.HomeView.as_view(), name="home"),

	# DEFINE URL FOR CLIENTS

	path("clients/", views.ClientListView.as_view(), name="client_list"),
	path("clients/create/", views.ClientCreateView.as_view(), name="client_create"),
	path("clients/<int:pk>/update/", views.ClientUpdateView.as_view(), name="client_update"),
	path("clients/<int:pk>/delete/", views.ClientDeleteView.as_view(), name="client_delete"),
	
	# DEFINE URL FOR LAWYERS

	path("lawyers/", views.LawyerListView.as_view(), name="lawyer_list"),
	path("lawyers/create/", views.LawyerCreateView.as_view(), name="lawyer_create"),
	path("lawyers/<int:pk>/update/", views.LawyerUpdateView.as_view(), name="lawyer_update"),
	path("lawyers/<int:pk>/delete/", views.LawyerDeleteView.as_view(), name="lawyer_delete"),

	# DEFINE URL FOR CASES

	path("cases/", views.CaseListView.as_view(), name="case_list"),
	path("cases/create/", views.CaseCreateView.as_view(), name="case_create"),
	path("cases/<int:pk>/update/", views.CaseUpdateView.as_view(), name="case_update"),
	path("cases/<int:pk>/delete/", views.CaseDeleteView.as_view(), name="case_delete"),




]
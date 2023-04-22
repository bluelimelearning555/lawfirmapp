"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


"""
#The include function is used to include other URL patterns from other
# modules or apps in your project. This allows you to organize your
# URL patterns into separate modules or apps and then
# include them in the main urls.py file of your project.



from django.contrib import admin
from django.urls import  include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("cases.urls", namespace="cases")),
]



'''
The include function is used to include the URL patterns of another app
in the current urls.py file, and the string "cases.urls" 
specifies the module that contains the URL patterns for the cases app.

The namespace parameter is used to set a namespace for the included 
URL patterns. A namespace is a way to organize URL patterns and
avoid naming conflicts with other URL patterns in your project. 
In this case, the namespace "cases" is assigned to the included URL patterns.


'''
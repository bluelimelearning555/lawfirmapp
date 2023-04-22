from django.contrib import admin

# Register your models here.


from .models import Client , Case, Lawyer


admin.site.register(Client)

admin.site.register(Case)

admin.site.register(Lawyer)
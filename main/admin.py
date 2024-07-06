from django.contrib import admin
from main.models import Blog, Contact, Project, Subscriber

# Register your models here.
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Subscriber)

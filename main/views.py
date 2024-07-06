from django.shortcuts import render
from django.views import View
from main.models import Blog
# Create your views here.


class IndexView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, "index.html", {'blogs': blogs})


class BLogView(View):
    def get(self, request, id):
        blogs = Blog.objects.filter(id=id)
        return render(request, "blog.html", {'blogs': blogs})


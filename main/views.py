from django.shortcuts import render, redirect
from django.views import View
from main.models import Blog, Project, Subscriber
from main.forms import ContactForm
from django.contrib import messages
# Create your views here.


class IndexView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        projects = Project.objects.all()
        form = ContactForm()
        return render(request, "index.html", {'blogs': blogs, 'projects': projects, 'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully")
            return redirect("/")
        return render(request, "index.html", {'form': form})


class BLogView(View):
    def get(self, request, id):
        blogs = Blog.objects.filter(id=id)
        return render(request, "blog.html", {'blogs': blogs})


class ProjectView(View):
    def get(self, request, id):
        project = Project.objects.filter(id=id)
        return render(request, "project.html", {'project': project})


class SubscribeView(View):

    def post(self, request):
        email = request.POST.get('email')
        Subscriber.objects.create(email=email)
        messages.success(request, "Thank You For Subscribing")
        return redirect('/')
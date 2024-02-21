from django.shortcuts import render
from .models import Project
from django.views import generic
# Create your views here.


def home(request):
    return render(request, 'home.html')


def education(request):
    return render(request, 'education.html')


def contacts(request):
    return render(request, 'contacts.html')


class ProjectListView(generic.ListView):
    model = Project
    template_name = 'list.html'
    context_object_name = 'projects'


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'detail.html'
    context_object_name = 'project'
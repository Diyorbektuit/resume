from .models import Project
from django.views import generic
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Xabaringiz jo'natildi.Rahmat!")
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})




def home(request):
    return render(request, 'home.html')


def education(request):
    return render(request, 'education.html')


class ProjectListView(generic.ListView):
    model = Project
    template_name = 'list.html'
    context_object_name = 'projects'


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'detail.html'
    context_object_name = 'project'
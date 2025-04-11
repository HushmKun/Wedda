from typing import override
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import Testmonial, Service, Tag, Project

from .forms import ContactForm
from django.shortcuts import render, redirect

from django.contrib.messages import constants as messages
from django.contrib import messages as msg

MESSAGE_TAGS = {
    messages.SUCCESS: "success",
    messages.WARNING: "warning",
    messages.ERROR: "danger"
}

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class HomeView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all() 
        context["testimonials"] = Testmonial.objects.all() 
        return context
        
class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = 28
        context['clients'] = 15
        context['teams'] = 3
        context['testimonials'] = Testmonial.objects.all()
        return context
    
class ServicesView(TemplateView):
    template_name = "main/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all() 
        return context

class ServiceView(DetailView):
    template_name = "main/service.html"
    model = Service
    context_object_name = "service"

    @override
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)	
        context['services'] = Service.objects.all()
        return context    

class ShowcaseView(TemplateView):
    template_name = "main/showcase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['projects'] = Project.objects.all()
        return context

class ProjectView(DetailView):
    template_name = "main/project.html"
    model = Project
    context_object_name = "project"

    @override
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)	

        try:
            context['prev_item'] = Project.objects.get(pk=self.object.id - 1)
        except: 
            context['prev_item'] = None
        
        try:
            context['next_item'] = Project.objects.get(pk=self.object.id + 1)
        except:
            context['next_item'] = None

        
        return context    

def ContactFormView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            msg.add_message(request, messages.SUCCESS, "Message sent successfully.")
            return redirect('index')
        else: 
            msg.add_message(request, messages.WARNING, "Message was not sent successfully.")
            return redirect('contact')
        

    elif request.method == "GET":
        form = ContactForm()
        context = {"form": form}
        return render(request, "main/contact.html", context)
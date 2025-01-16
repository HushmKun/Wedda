from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView

from .models import newsletter


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class HomeView(CreateView):
    template_name = "main/index.html"
    model = newsletter
    fields = ['email']

    def get_success_url(self):
        return reverse('index')
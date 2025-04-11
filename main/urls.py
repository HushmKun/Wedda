from django.urls import path
from .views import HomeView, ServicesView, AboutView, ContactFormView, ServiceView, ShowcaseView, ProjectView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('service/', ServicesView.as_view(), name='services'),
    path('contact/', ContactFormView, name='contact'),
    path('service/<int:pk>', ServiceView.as_view(), name='single_service'),
    path('showcase/', ShowcaseView.as_view(), name='showcase'),
    path('showcase/<int:pk>', ProjectView.as_view(), name='single_project'),


]

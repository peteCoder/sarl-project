
from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.home, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('faqs/', views.faqs, name="faqs"),
    # path('not-found/', views.not_found, name="not_found"),
    path('project/', views.project, name="project"),
    path('team/', views.team, name="team"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('blog/', views.blog, name="blog"),
    path('service/', views.service, name="service"),
    path('destinations/', views.destinations, name="destinations"),
]



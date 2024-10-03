from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def faqs(request):
    return render(request, 'faqs.html', {})



def project(request):
    return render(request, 'project.html', {})


def service(request):
    return render(request, 'service.html', {})


def team(request):
    return render(request, 'team.html', {})


def testimonial(request):
    return render(request, 'testimonial.html', {})

def destinations(request):
    return render(request, 'destinations.html', {})




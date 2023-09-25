from django.shortcuts import render
from .models import Card , Contact

def index(request):
    card = Card.objects.all()
    return render(request, 'index.html', {'card': card})


def vehicle(request):
    return render(request, 'vehicle.html')

def about(request):
    return render(request, 'about.html')

def desire(request):
    return render(request, 'desire.html')

def confidence(request):
    return render(request, 'confidence.html')

def think(request):
    return render(request, 'think.html')

def idea(request):
    return render(request, 'idea.html')

def rich(request):
    return render(request, 'rich.html')

def conc(request):
    return render(request, 'conc.html')

def contact(request):
    if request.method == "POST":  # Use "POST" in uppercase
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('Suggestion', '')  # Use the correct field name
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'contact.html')


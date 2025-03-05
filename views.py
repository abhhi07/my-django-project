from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Loads your HTML file
from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after saving
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {'form': form})

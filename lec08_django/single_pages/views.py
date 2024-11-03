from django.shortcuts import render
import pandas as pd
# Create your views here.
def home(request):
    return render(request, 'single_pages/index.html', {'title': 'Home', 'nav-active':'index', 'css':'index'} )

def index(request):
    return render(request, 'single_pages/index.html', {'title': 'index', 'nav-active':'index', 'css':'index'} )

def careers(request):
    education_list = pd.read_csv("single_pages/education.csv").to_dict(orient='records')
    careers_list = pd.read_csv("single_pages/careers.csv").to_dict(orient='records')
    return render(request, 'single_pages/careers.html', {'title':'careers', 'nav_active':'careers', 'education_list':education_list, 'careers_list':careers_list})

def contact(request):
    return render(request,'single_pages/contact.html', {'title':'contact', 'nav_active':'contact'})

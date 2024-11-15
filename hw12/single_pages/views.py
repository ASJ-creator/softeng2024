from django.shortcuts import render
import pandas as pd

# Create your views here.

def index(request):
    return render(request, 'single_pages/index.html', {'title': 'Home', 'nav_active': 'index', 'css': 'index'})

def about(request):
    education_list = pd.read_csv("single_pages/education.csv").to_dict(orient='records')
    careers_list = pd.read_csv("single_pages/careers.csv").to_dict(orient='records')
    return render(request, 'single_pages/careers.html', {'title': 'About', 'nav_active': 'careers', 'education':education_list, 'careers':careers_list})

def contact(request):
    return render(request, 'single_pages/contact.html', {'title': 'Contact', 'nav_active': 'contact'})

def blog(request):
    articles = [
        {'title': 'Post 1', 'content': 'This is the content of the first blog post.'},
        {'title': 'Post 2', 'content': 'This is the content of the second blog post.'},
        {'title': 'Post 3', 'content': 'This is the content of the third blog post.'},
        {'title': 'Post 4', 'content': 'This is the content of the fourth blog post.'},
        {'title': 'Post 5', 'content': 'This is the content of the fifth blog post.'},
    ]
    return render(request, 'single_pages/blog.html', {'title': 'Blog', 'nav_active': 'blog', 'articles': articles})
from django.shortcuts import render

def home(request):
    context={}
    return render(request, 'collatio/home.html', context)

def search(request):
    context={}
    return render(request, 'collatio/search.html', context)

def categories(request):
    context={}
    return render(request, 'collatio/category.html', context)

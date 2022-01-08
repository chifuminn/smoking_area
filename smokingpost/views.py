from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def age_confirmation_view(request):
    return render(request, 'age_confirmation.html')

def detail_view(request):
    return render(request, 'detail.html')

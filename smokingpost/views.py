from django.shortcuts import render
from .models import SmokingAreaModel

def index_view(request):
    smoking_area_list = SmokingAreaModel.objects.all()
    return render(request, 'index.html',{'smoking_area_list':smoking_area_list})

def age_confirmation_view(request):
    return render(request, 'age_confirmation.html')

def detail_view(request):
    return render(request, 'detail.html')

from django.shortcuts import render
from .models import SmokingAreaModel

def age_confirmation_view(request):
    return render(request, 'age_confirmation.html')

def top_view(request):
    # TODO: 最新6件を表示したい
    smoking_area_list = SmokingAreaModel.objects.order_by("-postdate")
    return render(request, 'top.html',{'smoking_area_list':smoking_area_list})

def detail_view(request, pk):
    object = SmokingAreaModel.objects.get(pk=pk)
    return render(request, 'detail.html', { 'object': object })

def warning_view(request):
    return render(request, 'warning.html')

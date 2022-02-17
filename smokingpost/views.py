from django.shortcuts import render
from .models import SmokingAreaModel
from django.contrib import messages
from django.db.models import Q

def age_confirmation_view(request):
    return render(request, 'age_confirmation.html')

def top_view(request):
    # TODO: 最新6件を表示したい
    smoking_area_list = SmokingAreaModel.objects.order_by("-postdate")
    keyword = request.GET.get('keyword')

    if keyword:
        smoking_area_list = smoking_area_list.filter(
            Q(name__icontains=keyword)
        )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    
    return render(request, 'top.html',{'smoking_area_list':smoking_area_list})

def detail_view(request, pk):
    object = SmokingAreaModel.objects.get(pk=pk)
    return render(request, 'detail.html', { 'object': object })

def warning_view(request):
    return render(request, 'warning.html')

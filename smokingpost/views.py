from django.shortcuts import render
from .models import SmokingAreaModel
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError

@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)

def age_confirmation_view(request):
    return render(request, 'age_confirmation.html')

def top_view(request):
    cookie = request.COOKIES.get('age_auth_token')
    if cookie:
        # TODO: 最新6件を表示したい
        smoking_area_list = SmokingAreaModel.objects.order_by("-postdate")
        keyword = request.GET.get('keyword')

        if keyword:
            smoking_area_list = smoking_area_list.filter(
                Q(name__icontains=keyword)
            )
            messages.success(request, '「{}」の検索結果'.format(keyword))
        
        return render(request, 'top.html',{'smoking_area_list':smoking_area_list})
    else:
        return render(request, 'age_confirmation.html')

def after_auth_top_view(request):
    smoking_area_list = SmokingAreaModel.objects.order_by("-postdate")
    keyword = request.GET.get('keyword')
    response = render(request, 'top.html',{'smoking_area_list':smoking_area_list})
    response.set_cookie('age_auth_token', '98128322887')

    if keyword:
        smoking_area_list = smoking_area_list.filter(
            Q(name__icontains=keyword)
        )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    
    return response

def detail_view(request, pk):
    cookie = request.COOKIES.get('age_auth_token')
    if cookie:
        object = SmokingAreaModel.objects.get(pk=pk)
        return render(request, 'detail.html', { 'object': object })
    else:
        return render(request, 'age_confirmation.html')

def warning_view(request):
    return render(request, 'warning.html')

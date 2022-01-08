from django.urls import path
from .views import index_view, age_confirmation_view, detail_view

urlpatterns = [
    path('', index_view, name='index'),
    path('age_confirmation/', age_confirmation_view, name='age_confirmation'),
    path('detail/', detail_view, name='detail'),
]

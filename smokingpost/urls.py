from django.urls import path
from .views import top_view, age_confirmation_view, detail_view, warning_view, after_auth_top_view

urlpatterns = [
    path('', age_confirmation_view, name='age_confirmation'),
    path('warning/', warning_view, name='warning'),
    path('top/', top_view, name='top'),
    path('after-auth-top', after_auth_top_view, name='after_auth_top'),
    path('detail/<int:pk>/', detail_view, name='detail'),
]

from django.urls import path, include
from . import views

app_name = "quotaapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('quota_request/', views.quota_request, name='quota_request'),
    path('quota_semester2/', views.quota_semester2, name='quota_semester2'),
    path('cancel/<str:course>', views.cancel, name='cancel'),
    path('request/<str:course>', views.request, name='request'),
    path('complete/', views.complete, name='complete'),
]

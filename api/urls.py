from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.urlList, name='url-list'),
    path('url-create/', views.urlCreate, name='url-create')

]

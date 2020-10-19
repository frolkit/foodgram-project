from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.Index.as_view(), name='index_test'),
]

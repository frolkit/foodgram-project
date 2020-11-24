from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('tech/', views.tech, name='tech'),
    path('recipe_create/', views.recipe_create, name='recipe_create'),
    path('subscribe_list/', views.subscribe_list, name='subscribe_list'),
    path('purchase_list/', views.purchase_list, name='purchase_list'),
    path('purchase_list/download/', views.purchase_list_download,
         name='purchase_list_download'),
    path('favorite_list/', views.favorite_list, name='favorite_list'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/<recipe_id>/', views.recipe, name='recipe'),
    path('<username>/<recipe_id>/edit/', views.recipe_edit,
         name='recipe_edit'),
    path('<username>/<recipe_id>/delete/',
         views.recipe_delete, name='recipe_delete'),
]

from django.urls import path

from . import views


urlpatterns = [
    path('purchases/', views.PurchaseView.as_view(), name='api_purchase'),
    path('purchases/<int:pk>/', views.PurchaseView.as_view(),
         name='api_purchase_delete'),
    path('favorites/', views.FavoriteView.as_view(), name='api_favorite'),
    path('favorites/<int:pk>/', views.FavoriteView.as_view(),
         name='api_favorite_delete'),
    path('subscriptions/', views.SubscribeView.as_view(), name='api_favorite'),
    path('subscriptions/<int:pk>/', views.SubscribeView.as_view(),
         name='api_favorite_delete'),
    path("ingredients/", views.IngredientView.as_view()),
]

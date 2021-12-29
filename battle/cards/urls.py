from django.urls import path

from . import views

urlpatterns = [
    path('', views.CardListView.as_view(), name='card_list'),
    path('card/<int:pk>', views.CardDetailView.as_view(), name='card_detail'),
    path('card_delete/<int:pk>', views.CardDeleteView.as_view(), name='card_delete'),
    path('card_update/<int:pk>', views.CardUpdateView.as_view(), name='card_update'),
    path('create', views.CardCreateView.as_view(), name='card_create'),
]
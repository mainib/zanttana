from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListZantta.as_view()),
    path('<int:pk>/', views.DetailZantta.as_view()),
]
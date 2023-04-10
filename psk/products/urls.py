from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('products/plazma', views.plazma, name = 'plazma'),
    path('products/lazer', views.Lazer, name = 'lazer'),
    path('products/welding', views.Welding, name = 'welding'),
    path('about/', views.about, name = 'about'),
]

from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<str:type>/', views.company, name='company'),
    path('products/<str:type>/<str:company>/', views.model, name='models'),
    path(
        'products/<str:type>/<str:company>/<slug:slug>/',
        views.Products,
        name='products',
    ),
]

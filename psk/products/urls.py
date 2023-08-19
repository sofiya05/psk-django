from django.urls import path


from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
   # path('products/plazma/', views.Plazma, name='plazma'),
    path('products/<str:type>/', views.Test, name='test'),
    path('products/plazma/<slug:slug>', views.Products, name = 'products'),
    path('products/lazer/', views.Lazer, name='lazer'),
    path('products/welding/', views.Welding, name='welding'),
]

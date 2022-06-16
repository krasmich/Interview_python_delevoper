from django.urls import path

from . import views

app_name = 'goods_app'

urlpatterns = [
    path('', views.all_goods, name='all_goods'),
    path('<slug:category_slug>/', views.category_list, name='category_list'),
]

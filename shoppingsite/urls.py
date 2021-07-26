from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.make_post, name='new'),
    path('<str:id>', views.detail, name='detail'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('search/', views.search, name='search'),
]
from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('stock_tracker/', views.stock_tracker, name= 'stock_tracker'),
]

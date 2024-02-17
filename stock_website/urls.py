from django.contrib import admin
from django.urls import path
from website import views as website_views
from api import views as api_views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', website_views.home, name= 'home'),
    path('stock_tracker/', website_views.stock_tracker, name= 'stock_tracker'),
    path('api/', api_views.api_home)
]

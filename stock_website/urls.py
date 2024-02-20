from django.contrib import admin
from django.urls import path
from website import views as website_views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', website_views.home, name= 'home'),
    path('stock_picker/', website_views.stock_picker, name= 'stock_picker'),
    path('stock_tracker/', website_views.stock_tracker, name= 'stock_tracker'),
]

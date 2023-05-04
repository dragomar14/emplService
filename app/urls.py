from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('src.authentication.urls')),
    path('api/employees/', include('src.employees.urls')),
    path('api/restaurants/', include('src.restaurants.urls')),
    path('api/menus/', include('src.menus.urls')),
]

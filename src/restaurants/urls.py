from django.urls import include, path


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('restaurants.urls')),
]

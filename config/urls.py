from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/temples/', include('locations.urls')),
    path('api/slots/', include('slots.urls')),
    path('api/bookings/', include('bookings.urls')),
]
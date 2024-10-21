from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),  # Prefix app1's URLs with app1/
    path('app2/', include('app2.urls')),  # Include app2's URLs under app2/
]

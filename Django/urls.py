from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('view_table/', include('view_table.urls')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from tasks import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/',include('tasks.urls'))
]

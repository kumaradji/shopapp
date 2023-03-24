
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py)
    # # подключались к главному приложению с префиксом products/.
    path('products/', include('simpleapp.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
]

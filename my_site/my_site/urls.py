from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog_app.urls')),
    path('admin/', admin.site.urls),
]

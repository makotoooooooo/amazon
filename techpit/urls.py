from django.contrib import admin
from django.urls import path
from django.conf.urls import include # [2-3]追加
from django.conf import settings # [2-3]追加
from django.conf.urls.static import static

urlpatterns = [
    path('techpit/admin/', admin.site.urls),
    path('techpit/amazon/', include('amazon.urls')) # [2-3]追加
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


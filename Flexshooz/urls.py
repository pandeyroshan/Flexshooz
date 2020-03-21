from django.contrib import admin
from django.urls import path
from store import views as store_view
from management import views as manage_view
from users import views as user_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',store_view.index,name='homepage'),
    path('login/',user_view.login,name='login')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path
from store import views as store_view
from management import views as manage_view
from users import views as user_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',store_view.index,name='homepage'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('register/',user_view.register,name='register'),
    path('logout/',auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),name='logout'),
    path('add_to_cart/<int:p_id>',store_view.add_to_cart,name='add_to_cart'),
    path('add_to_wishlist/<int:p_id>',store_view.add_to_wishlist,name='add_to_wishlist'),
    path('remove_from_cart/<int:p_id>',store_view.remove_from_cart,name='remove_from_wishlist'),
    path('remove_from_wishlist/<int:p_id>',store_view.remove_from_wishlist,name='remove_from_wishlist'),
    path('cart/',store_view.get_cart,name='cart'),
    path('remove/<int:id>',store_view.remove_from_cart,name='remove_cart')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView, LogoutView 

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/register/', views.registration, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('new-product/', views.postproduct, name='newproduct'),
    path('product/<id>', views.get_product, name='product'),
    path('search/', views.search_products, name='search_products'),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
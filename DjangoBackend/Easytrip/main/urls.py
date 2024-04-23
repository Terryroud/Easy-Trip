from django.conf import settings
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about , name = 'about'),
    path('user', views.user , name = 'user'),
    path('register/', views.register, name='register'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
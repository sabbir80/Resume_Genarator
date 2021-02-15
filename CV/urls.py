from django.conf.urls.static import static
from django.urls import path
from .views import login
from . import views
from Resume1 import settings

urlpatterns = [
                  path('login/', views.login, name='login'),
                  path('registration/', views.registration, name='registration'),
    path('', views.home, name='home')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

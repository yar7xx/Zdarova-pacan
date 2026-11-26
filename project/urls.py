from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views # Импортируем встроенные вьюхи

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Маршруты для входа и выхода
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('tasks/', include('app.urls')),
    path('', RedirectView.as_view(pattern_name='tasks:list', permanent=False)),
]
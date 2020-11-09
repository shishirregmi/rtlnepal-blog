"""rtlnepal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    #url(r'^accounts/login/$',views.login,name='login'),
    #url(r'^accounts/logout/$',views.logout,name='logout',kwargs={'next_page':'/'}),
    path("accounts/login/", views.LoginView.as_view(template_name="registration/login.html"),name="login"),
    path("accounts/logout/", views.LogoutView.as_view(template_name="registration/logout.html"),name="logout"),
 
]


if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
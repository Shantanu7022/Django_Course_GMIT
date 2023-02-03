"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from mainapp import views

urlpatterns = [
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('home/',views.homepage, name="homepage"),
    path('',views.homepage, name="homepage"),
    path('about/',views.about, name="about"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('contact/',views.contact, name="contact"),
    path('signup/',views.user_signup, name="usersignup"),
    path('login/',views.user_login,name="login"),
    path('addpost/',views.addpost,name="addpost"),
    path('updatepost/<int:id>/',views.updatepost,name="updatepost"),
    path('deletepost/<int:id>/',views.deletepost,name="deletepost"),
    path('logout/',views.user_logout,name="logout"),
    path('oauth/', include('social_django.urls', namespace='social')),
    
    
]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



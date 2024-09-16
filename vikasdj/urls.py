"""
URL configuration for vikasdj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Home page
    # path('about/', views.about, name='about'),    # About page
    # path('navbar/', views.navbar, name='navbar'),   # Navbar page (currently commented)
    # path('back/', views.index1, name='index1'),  # Back page
    # path('removepunc/', views.removepunc, name='removepunc'),  # Remove punctuation page
    path('analyze/', views.analyze, name='analyze'),  # Analyze page
]
 
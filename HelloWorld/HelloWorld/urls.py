"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views.py. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views.py
    1. Add an import:  from my_app import views.py
    2. Add a URL to urlpatterns:  path('', views.py.home, name='home')
Class-based views.py
    1. Add an import:  from other_app.views.py import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.conf.urls import url

from . import views,testdb
from . import search, search2
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$', views.hello),
    path('runoob/', views.runoob),
    path('testdb/', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
]
from django.conf.urls import url, include
from django.contrib import admin

from lists import views as lists_views
from lists import urls as lists_urls

urlpatterns = [
    url(r"^$", lists_views.home_page, name="home"),
    url(r"^lists/", include(lists_urls)),
]

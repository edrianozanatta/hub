from django.conf.urls import include, url
from django.conf.urls.static import static

from .views import *

app_name = "site"

urlpatterns = [
    url(r'^$', home, name='home'),
]

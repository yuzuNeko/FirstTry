from django.conf.urls import url,include
from . import views
urlpatterns = [
    
    url('^page1/index/',views.index),
    url('^page1/show/',views.show),
    url('^page1/show2/',views.show2),
]
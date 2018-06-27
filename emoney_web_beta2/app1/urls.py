from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^page1/',views.index),
    url(r'page2/',views.data1),
    url('page3/',views.data2),
    url('page4/',views.data3),
    url(r'^page5/homework0614',views.homework0614),
    url('^page5/0618img',views.img0618),
    url('^page5/crawl',views.crawl_day)
]
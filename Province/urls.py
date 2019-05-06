from django.conf.urls import url
from Province import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^maker/',views.myMaker,name='maker'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profits', views.profits, name='profits'),
    path('store', views.store, name='store'),

]

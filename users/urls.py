from django.urls import path
from . import views

urlpatterns = [
    path('account', views.show_acc, name='accounts'),
    path('logout', views.signout, name='signout')
]

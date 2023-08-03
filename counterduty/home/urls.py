from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('staff/', views.staffadd),
    path('stafflist/', views.stafflist),
    path('stafflist/<int:id>', views.staffdetails),
]
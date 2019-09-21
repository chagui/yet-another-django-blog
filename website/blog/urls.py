from django.urls import path

from . import views

urlpatterns = [
    path('post/<int:pk>', views.PostView.as_view(), name='post'),
]

from django.urls import path
from autodonate_placeholder_plugin import views

urlpatterns = [
    path('', views.index, name="placeholder-index")
]

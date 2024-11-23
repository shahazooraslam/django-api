from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/",views.BlogpostListCreate.as_view(),name="blg"),
    path("blogpost/<int:pk>/",views.BlogPostRetriveUpdateDestroy.as_view(),name="upd")
]

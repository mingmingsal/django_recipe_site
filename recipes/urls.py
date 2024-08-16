from django.urls import path

from . import views
app_name = "recipes"

urlpatterns = [
    path("", views.IndexView.as_view(), name="recipe-index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
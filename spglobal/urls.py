from django.urls import path
from . import views

urlpatterns = [
    path("", views.fetch_data, name="fetch_data"),
    path(
        "constituents/<str:index_code>/",
        views.fetch_index_constituents,
        name="fetch_index_constituents",
    )
]
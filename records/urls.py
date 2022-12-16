from django.urls import path
from records.views import list_categories, list_details, log_event

urlpatterns = [
    path("", list_categories, name="list_categories"),
    path("log/<int:id>/", list_details, name="list_details"),
    path("log_event/", log_event, name="log_event"),
]

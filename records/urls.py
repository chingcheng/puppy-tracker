from django.urls import path
from records.views import list_categories, category_details, log_event, edit_event

urlpatterns = [
    path("", list_categories, name="list_categories"),
    path("category/<str:category_name>/", category_details, name="category_details"),
    path("log-event/<str:category_name>/", log_event, name="log_event"),
    path("log-event/blank/", log_event, name="log_blank_event"),
    path("edit-event/<int:id>/", edit_event, name="edit_event"),
]

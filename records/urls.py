from django.urls import path
from records.views import list_categories, log_event, category_details

urlpatterns = [
    path("", list_categories, name="list_categories"),
    # path("log/<int:id>/", list_details, name="list_details"),
    path("log_event/", log_event, name="log_event"),
    path("<str:category_name>/", category_details, name="cat_details"),
]

from django.urls import path
from .place_api import PlaceListView, PlaceCreateView, PlaceRetriveView, PlaceUpdateView, PlaceDestroyView

urlpatterns = [
    path('places/', PlaceListView.as_view(), name="places"),
    path('places/create', PlaceCreateView.as_view(), name="place_create"),
    path('places/<int:id>/', PlaceRetriveView.as_view(), name="place"),
    path('places/<int:id>/update/', PlaceUpdateView.as_view(), name="place_update"),
    path('places/<int:id>/delete/', PlaceDestroyView.as_view(), name="place_delete")
]

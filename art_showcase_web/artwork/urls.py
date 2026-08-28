from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artwork/<int:artwork_id>/", views.get_artwork, name="get_artwork"),
    path("artworks/", views.get_all_artworks, name="get_all_artworks"),
    path("artworks/by_tags/", views.get_artwork_by_tags, name="get_artwork_by_tags"),
    path("artwork/create/", views.create_artwork, name="create_artwork"),
    path("artwork/update/<int:artwork_id>/", views.update_artwork, name="update_artwork"),
    path("artwork/remove/<int:artwork_id>/", views.remove_artwork, name="remove_artwork"),
]
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from artwork.models import Artwork

# "artworks/"
def index(request):
    return HttpResponse("Hello, world. You're at the artwork index.")

# "artwork/<int:artwork_id>/"
def get_artwork(request, artwork_id):
    specific_artwork = Artwork.objects.get(id=artwork_id)
    return HttpResponse(specific_artwork)

# "artworks/"
def get_all_artworks(request):
    all_artworks = Artwork.objects.all()
    template = loader.get_template("artwork/showcase_artworks.html")
    context = {
        "artwork_list": all_artworks,
    }
    return HttpResponse(template.render(context, request))

# "artworks/by_tags/"
def get_artwork_by_tags(request):
    tags = request.GET.getlist("tags")
    artworks = Artwork.objects.filter(tags__name__in=tags).distinct()
    template = loader.get_template("artwork/showcase_artworks.html")
    context = {
        "artwork_list": artworks,
    }
    return HttpResponse(template.render(context, request))

# "artwork/create/"
def create_artwork(request):
    title = request.POST.get("title")
    location = request.POST.get("location")
    type_of_art_id = request.POST.get("type_of_art_id")
    tags = request.POST.getlist("tags")
    artwork = Artwork.objects.create(title=title, location=location, typeofArt_id=type_of_art_id)
    artwork.tags.set(tags)
    return HttpResponse(artwork)

# "artwork/update/<int:artwork_id>/"
def update_artwork(request, artwork_id):
    artwork = Artwork.objects.get(id=artwork_id)
    title = request.POST.get("title")
    location = request.POST.get("location")
    type_of_art_id = request.POST.get("type_of_art_id")
    tags = request.POST.getlist("tags") 
    artwork.update(title=title, location=location, typeofArt_id=type_of_art_id)
    artwork.tags.set(tags)
    return HttpResponse(artwork)

# "artwork/remove/<int:artwork_id>/"
def remove_artwork(request, artwork_id):
    artwork = Artwork.objects.get(id=artwork_id)
    artwork.delete()
    return HttpResponse(f"Artwork with id {artwork_id} has been removed.")
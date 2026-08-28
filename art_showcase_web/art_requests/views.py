from django.http import HttpResponse
from django.shortcuts import render

from art_showcase_web.art_requests.models import ArtRequest

# Create your views here.

# 
def send_request(request):
    category = request.POST.get("category")
    deadline = request.POST.get("deadline")
    description = request.POST.get("description")
    done = False
    art_request = ArtRequest.objects.create(category=category, deadline=deadline, description=description, done=done)
    art_request.save()
    return HttpResponse(art_request)

def get_requests(request):
    art_requests = ArtRequest.objects.all()
    return HttpResponse(art_requests)

def get_request(request, request_id):
    art_request = ArtRequest.objects.get(id=request_id)
    return HttpResponse(art_request)

def get_request_by_tags(request):
    tags = request.GET.getlist("tags")
    art_requests = ArtRequest.objects.filter(category__name__in=tags).distinct()
    return HttpResponse(art_requests)

def finish_request(request, request_id):
    art_request = ArtRequest.objects.get(id=request_id)
    art_request.done = True
    art_request.save()
    return HttpResponse(art_request)

def change_request(request, request_id):
    art_request = ArtRequest.objects.get(id=request_id)
    category = request.POST.get("category")
    deadline = request.POST.get("deadline")
    description = request.POST.get("description")
    done = request.POST.get("done")
    art_request.category = category
    art_request.deadline = deadline
    art_request.description = description
    art_request.done = done
    art_request.save()
    return HttpResponse(art_request)

def remove_request(request, request_id):
    art_request = ArtRequest.objects.get(id=request_id)
    art_request.delete()
    return HttpResponse(f"Art request with id {request_id} has been removed.")


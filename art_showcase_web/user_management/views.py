from django.http import HttpResponse
from django.shortcuts import render

from art_showcase_web.user_management.models import User

# Create your views here.
def create_user(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    isBlocked = False
    isAdmin = False
    user = User.objects.create(username=username, email=email, password=password, isBlocked=isBlocked, isAdmin=isAdmin)
    user.save()
    return HttpResponse(user)

def login_user(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    try:
        user = User.objects.get(email=email, password=password)
        return HttpResponse(user)
    except User.DoesNotExist:
        return HttpResponse("Invalid email or password.")

def block_user(request, blocking_user_id, blocked_user_id):
    blocking_user = User.objects.get(id=blocking_user_id)
    if not blocking_user.isAdmin:
        return HttpResponse("You do not have permission to block users.")
    blocked_user = User.objects.get(id=blocked_user_id)
    blocked_user.isBlocked = True
    blocked_user.save()
    return HttpResponse(blocked_user)

def update_admin(request, user_id):
    user = User.objects.get(id=user_id)
    user.isAdmin = True
    user.save()
    return HttpResponse(user)

def create_admin(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    isBlocked = False
    isAdmin = True
    user = User.objects.create(username=username, email=email, password=password, isBlocked=isBlocked, isAdmin=isAdmin)
    user.save()
    return HttpResponse(user)

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return HttpResponse(f"User with id {user_id} has been deleted.")
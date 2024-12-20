from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "Welcome to the Social Media API!"})

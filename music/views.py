from django.http import HttpResponse
def index(request):
    return HttpResponse("this is music app")

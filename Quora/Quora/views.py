from django.http import HttpResponse

# Class Home 
def home(requests):
    return HttpResponse("Test")
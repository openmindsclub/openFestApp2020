from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'pages/index/index.html', {})

# ERRROR HANDLING
def bad_request(request, exception):
    return render(request,'pages/errors/400.html')

def permission_denied(request, exception):
    return render(request,'pages/errors/403.html')

def page_not_found(request, exception):
    return render(request,'pages/errors/404.html')

def server_error(request):
    return render(request,'pages/errors/500.html')
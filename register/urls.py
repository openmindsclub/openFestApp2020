"""register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view
from django.conf.urls import handler400, handler403, handler404, handler500


urlpatterns = [
    # ADMIN SITE
    path('F4LL0UTN3WV3G45/', admin.site.urls),
    # OTHER
    path('', home_view, name = 'home'),
    path('home/', home_view, name = 'home')
]

# ERROR HANDLING 
handler400 = 'pages.views.bad_request'
handler403 = 'pages.views.permission_denied'
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

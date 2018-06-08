from django.contrib import admin
#from django.views.generic import RedirectView
from django.urls import include, path

urlpatterns = [
    path('notes/', include('notes.urls', namespace='notes')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import include, path

urlpatterns = [
    path('', RedirectView.as_view(url='notes/'), name='index'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('notes/', include('notes.urls', namespace='notes')),
    path('admin/', admin.site.urls),
]

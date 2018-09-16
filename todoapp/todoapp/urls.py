from django.conf.urls import url, include
from django.contrib import admin


api_urls = [
    url(r'^todos/', include('todos.urls')),
    url(r'', include('users.urls')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]

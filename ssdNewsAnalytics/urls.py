from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', include('ssdNewsAnalytics.apps.article.urls')),
    path('author/', include('ssdNewsAnalytics.apps.author.urls')),
    path('newspaper/', include('ssdNewsAnalytics.apps.newspaper.urls')),
    path('owner/', include('ssdNewsAnalytics.apps.owner.urls')),
    path('publisher/', include('ssdNewsAnalytics.apps.publisher.urls')),
    path('topic/', include('ssdNewsAnalytics.apps.topic.urls')),
]

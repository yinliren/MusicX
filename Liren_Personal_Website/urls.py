from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),

    # url(r'^', include('music.urls')),

    url(r'^oauth/', include('social_django.urls', namespace='social')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# urlpatterns = [
#     # path(r'admin/', admin.site.urls),
#     # path(r'music/',include('music.urls')),
#     # path(r'stockMarket/', views.StockList.as_view()),
#     url(r'^admin/', admin.site.urls),
#     url(r'^music/', include('music.urls')),
#     url(r'^', include('music.urls')),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

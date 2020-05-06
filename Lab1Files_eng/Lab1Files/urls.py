from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('ajax/add-download/', views.AjaxAddDownload.as_view()),
    path('admin-statistics/', views.AdminStatistics.as_view(),name='admin-statistics'),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
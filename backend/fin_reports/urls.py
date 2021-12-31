from django.conf.urls import url
from fin_reports import views

urlpatterns = {
    url(r'upload', views.upload),
    url(r'show_fin_reports', views.show_fin_reports),
    url(r'fin_reports', views.fin_reports),
}

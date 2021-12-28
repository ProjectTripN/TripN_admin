from django.conf.urls import url
from reservation import views

urlpatterns = {
    url(r'pre', views.preprocess),
    url(r'insert', views.insert_data),
    url(r'process/(?P<pk>\w{0,50})$', views.process),
    url(r'count', views.count_res),
    url(r'month', views.profit_month),
    url(r'year', views.profit_year)
}

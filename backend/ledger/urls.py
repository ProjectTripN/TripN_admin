from django.conf.urls import url
from ledger import views

urlpatterns = {
    url(r'pre_sales', views.pre_sales),
    url(r'pre_cost', views.cost),
    url(r'up_sales', views.upload_sales),
    url(r'up_cost', views.upload_cost),
    url(r'sales/(?P<pk>\w{0,50})$', views.sales),
    url(r'profit', views.profit),
    url(r'report', views.report_process),
    url(r'show_cost', views.show_cost)
}

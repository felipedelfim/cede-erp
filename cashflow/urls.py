from django.conf.urls import url

from . import views

app_name = 'cashflow'
urlpatterns = [
    url(r'^$', views.transaction_list, name='transaction_list'),
    url(r'^new/$', views.transaction_new, name='transaction_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.transaction_edit, name='transaction_edit'),
    url(r'^(?P<pk>\d+)/pay/$', views.transaction_pay, name='transaction_pay'),
    url(r'^(?P<pk>\d+)/remove/$', views.transaction_remove, name='transaction_remove'),
    url(r'^persons/$', views.person_list, name='person_list'),
    url(r'^persons/import/$', views.person_import, name='person_import'),
    url(r'^persons/new/$', views.person_new, name='person_new'),
    url(r'^persons/(?P<pk>\d+)/edit/$', views.person_edit, name='person_edit'),
    url(r'^persons/(?P<pk>\d+)/remove/$', views.person_remove, name='person_remove'),
    url(r'^items/$', views.item_list, name='item_list'),
    url(r'^items/import/$', views.item_import, name='item_import'),
    url(r'^items/(?P<pk>\d+)/value/$', views.item_get_value, name='item_get_value'),
    url(r'^items/(?P<pk>\d+)/inventory/$', views.item_inventory_add, name='item_inventory_add'),
    url(r'^items/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^items/(?P<pk>\d+)/remove/$', views.item_remove, name='item_remove'),
    url(r'^categories/(?P<pk>\d+)/items/$', views.category_items, name='category_items'),
    url(r'^reports/$', views.transaction_report, name='transaction_report'),

]

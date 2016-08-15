from django.conf.urls import url
from views import view_shop, view_shop_add, view_shop_ex

urlpatterns = [
    url(r'^$', view_shop),
    url(r'^addData$', view_shop_add),
    url(r'^viewEx$', view_shop_ex),
]

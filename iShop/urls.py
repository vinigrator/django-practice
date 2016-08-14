from django.conf.urls import url
from views import view_shop

urlpatterns = [
    url(r'^$', view_shop),
]

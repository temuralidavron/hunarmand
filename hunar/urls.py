from .views import AnketaView, AnketaGetingView, sample, InetgerView, DataItemView
from django.urls import path


urlpatterns = [
    path("anketaview/<int:id>",  AnketaView.as_view(), name='anketaview'),
    path("anketagetingview/",  AnketaGetingView.as_view(), name='anketaviewd'),
    path("inetgerview/",  InetgerView.as_view(), name='inetgerview'),
    path("data_item/<int:id>",  DataItemView.as_view(), name='data_item'),
    path("sample/",  sample),
]


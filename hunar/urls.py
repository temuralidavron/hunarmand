from .views import AnketaView, AnketaGetingView, sample, InetgerView
from django.urls import path


urlpatterns = [
    path("anketaview/<int:id>",  AnketaView.as_view(), name='anketaview'),
    path("anketagetingview/",  AnketaGetingView.as_view(), name='anketaviewd'),
    path("inetgerview/",  InetgerView.as_view(), name='inetgerview'),
    path("sample/",  sample),

]


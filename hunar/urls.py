from .views import AnketaView, AnketaGetingView, sample, InetgerView, DataItemView, AnketaEditView, HomeListView, \
    KengashView, ConfirmView, RejectionView
from django.urls import path


urlpatterns = [
    path("anketaview/<int:id>",  AnketaView.as_view(), name='anketaview'),
    path("anketaeditview/<int:id>",  AnketaEditView.as_view(), name='anketaeditview'),
    path("anketagetingview/",  AnketaGetingView.as_view(), name='anketaviewd'),
    path("inetgerview/",  InetgerView.as_view(), name='inetgerview'),
    path("data_item/<int:id>",  DataItemView.as_view(), name='data_item'),
    path("homelistiew/<int:id>",  HomeListView.as_view(), name='homelistiew'),
    path("kengashview",  KengashView.as_view(), name='kengashview'),
    path("confirmview",  ConfirmView.as_view(), name='confirmview'),
    path("rejectionview",  RejectionView.as_view(), name='rejectionview'),
    path("sample/",  sample),
]


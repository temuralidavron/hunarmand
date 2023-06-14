from .views import MarkanketaView, AnketaView, AnketaGetPostView, AnketaPostView, AnketaGetingView, AnketaViewGet, sample
from django.urls import path


urlpatterns = [

     # path("anketagetpostview/",  AnketaGetPostView.as_view(), name = 'anketagetpostview'),
    # path("markview/",  MarkView.as_view(), name = 'markview'),
    # path("anketagetview/<int:id>",  AnketaGetView.as_view(), name = 'anketagetview'),
     path("anketapostview/", AnketaPostView.as_view(), name = 'anketapostview'),
    # path("markanketaview/<int:id>",  MarkAnketaView.as_view(), name = 'markanketaview'),
    path("markanketaview/",  MarkanketaView.as_view(), name = 'markanketaview'),
    path("anketaview/",  AnketaView.as_view(), name = 'anketaview'),
    # path("anketagetview/",  AnketaGetView.as_view(), name = 'anketaview'),
    path("anketagetingview/",  AnketaGetingView.as_view(), name = 'anketaviewd'),
    path("anketaviewget/",  AnketaViewGet.as_view(), name = 'anketaviews'),
    # path("likeclass/<int:id>",  LikeClass.as_view()),


    path("sample/",  sample),

]


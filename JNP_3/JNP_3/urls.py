from django.conf.urls import *

urlpatterns = patterns('PhotoOrganizer.views',
                       (r"^(\d+)/$", "album"),
                       (r"^(\d+)/(full|thumbnails|edit)/$", "album"),
                       (r"^update/$", "update"),
                       (r"^search/$", "search"),
                       (r"^image/(\d+)/$", "image"),
                       (r"", "main"),
                       )

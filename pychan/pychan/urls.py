from django.conf.urls import patterns, include, url
from django.conf import settings
from rest_framework import routers
from engine import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'replies', views.ReplyViewSet)


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pychan.views.home', name='home'),
    # url(r'^pychan/', include('pychan.foo.urls')),
    url(r'^b/$', 'engine.views.ShowPostForm', name='ShowPostForm'),
    url(r'reply$', 'engine.views.ShowReplyForm', name='ShowReplyForm'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile', 'engine.views.ShowPostForm', name='ShowPostForm'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))
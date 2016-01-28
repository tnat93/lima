from django.conf.urls import patterns, url

from lima.views import IndexView

# TODO: add API endpoint urls
urlpatterns = patterns(
    '',

    url('^.*$', IndexView.as_view(), name='index'),
)

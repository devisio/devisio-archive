from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from devisio.journals.views import JournalCRUDView

urlpatterns = patterns('',
    url(r'^crud/journals/?$', JournalCRUDView.as_view(), name='journal-crud-view'),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
